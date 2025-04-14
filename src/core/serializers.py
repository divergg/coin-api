from rest_framework import serializers
from src.core.models import User, RewardLog, ScheduledReward




class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'coins',
        )


class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = RewardLog
        fields = (
            'user',
            'amount',
            'given_at',
        )


class ScheduledRewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduledReward
        fields = (
            'user',
            'amount',
            'execute_at'
        )
        read_only_fields = (
            'user',
            'execute_at'
        )
