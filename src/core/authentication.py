from django.utils import timezone
from drf_spectacular.extensions import OpenApiAuthenticationExtension
from rest_framework_simplejwt import authentication
from rest_framework_simplejwt.authentication import AuthUser
from rest_framework_simplejwt.tokens import Token



class JWTAuthenticationScheme(OpenApiAuthenticationExtension):
    target_class = 'src.core.authentication.JWTAuthentication'
    name = 'jwtAuth'

    def get_security_definition(self, auto_schema):
        return {'type': 'http', 'scheme': 'bearer', 'bearerFormat': 'JWT'}
