from django.urls import path, include
from rest_framework.routers import DefaultRouter

from src.core.views import TokenRefreshApiView, TokenVerifyApiView, MeViewSet, RewardViewSet

router = DefaultRouter(trailing_slash=False)
router.register('api/rewards', RewardViewSet, basename='rewards')

urlpatterns = [
    path('', include(router.urls)),
    path(
        'token-refresh',
        TokenRefreshApiView.as_view(),
        name='token-refresh',
    ),
    path('token-verify', TokenVerifyApiView.as_view(), name='token-verify'),
    path('api/profile', MeViewSet.as_view(), name='profile-data'),
]
