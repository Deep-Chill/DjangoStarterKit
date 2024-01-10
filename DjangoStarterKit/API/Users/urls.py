from .API_views import ProfileViewSet, ProfileSettingsViewSet

from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'profile', ProfileViewSet, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
    path('profile-settings/', ProfileSettingsViewSet.as_view({'put': 'update'}), name='api_profile_settings'),
]