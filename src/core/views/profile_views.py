from django.utils.translation import gettext_lazy as _
from drf_spectacular.utils import extend_schema
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from rest_framework import mixins, permissions, status, views, viewsets
from rest_framework.generics import ListAPIView
from rest_framework.exceptions import Throttled

from src.core.serializers import MeSerializer, RewardSerializer, ScheduledRewardSerializer
from src.core.services import RewardService
from src.core.throttle import RewardsUserThrottle


@extend_schema(tags=[_('Account')])
class MeViewSet(
    mixins.RetrieveModelMixin,
    GenericAPIView,
):

    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        return MeSerializer


    @extend_schema(operation_id='me', summary=_('Get profile'), responses=MeSerializer)
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )


@extend_schema(tags=[_('Rewards')])
class RewardViewSet(
    viewsets.GenericViewSet,
    ListAPIView,
):

    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = LimitOffsetPagination
    serializer_class = RewardSerializer


    @extend_schema(operation_id='rewards', summary=_('Get rewards'), responses=RewardSerializer)
    def list(self, request, *args, **kwargs):
        rewards = RewardService.retrieve_user_rewards(user=request.user)
        data = self.serializer_class(rewards, many=True)
        paginator = self.pagination_class()
        paginated_data = paginator.paginate_queryset(data, request)
        return paginator.get_paginated_response(paginated_data)

    @extend_schema(operation_id='request_reward', summary=_('Request a reward'), responses=ScheduledRewardSerializer, request=ScheduledRewardSerializer)
    @action(methods=['POST'], detail=False, url_path='request')
    def request_reward(self, request, *args, **kwargs):
        throttle = RewardsUserThrottle()
        if request.user.is_blocked:
            raise Throttled(
                detail='User is blocked',
            )
        if not throttle.allow_request(request, self):
            raise Throttled(detail='Too many requests')

        serializer = ScheduledRewardSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        amount = validated_data['amount']
        reward = RewardService.request_reward_for_user(user=request.user, amount=amount)
        output = ScheduledRewardSerializer(reward).data
        return Response(output, status=status.HTTP_201_CREATED)