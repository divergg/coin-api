from django.utils.translation import gettext_lazy as _
from drf_spectacular.utils import OpenApiExample, OpenApiResponse, extend_schema
from rest_framework_simplejwt.serializers import TokenRefreshSerializer, TokenVerifySerializer
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView




@extend_schema(
    tags=[_('Token')],
    summary='Refresh token',
    request=TokenRefreshSerializer,
    responses={
        200: OpenApiResponse(
            description='Successfully get new access token',
            examples=[
                OpenApiExample(
                    'Success',
                    value={'access': str},
                    status_codes=[200],
                )
            ],
        ),
        401: OpenApiResponse(
            description='Unauthorized',
            examples=[
                OpenApiExample(
                    'errors',
                    value=[
                        {
                            'code': 'token_not_valid',
                            'detail': 'Token is invalid',
                        },
                        {
                            'code': 'token_not_valid',
                            'detail': 'token_not_valid',
                        },
                    ],
                    status_codes=[401],
                ),
            ],
        ),
        400: OpenApiResponse(
            description='Bad request',
            examples=[
                OpenApiExample(
                    'errors',
                    value=[
                        {
                            'code': 'required',
                            'detail': 'This field is required.',
                        },
                    ],
                    status_codes=[400],
                ),
            ],
        ),
    },
)
class TokenRefreshApiView(TokenRefreshView):
    pass



@extend_schema(
    tags=[_('Token')],
    summary='Verify token',
    request=TokenVerifySerializer,
)
class TokenVerifyApiView(TokenRefreshView):
    pass
