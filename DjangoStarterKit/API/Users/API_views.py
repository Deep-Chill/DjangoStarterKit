from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, exceptions, generics, mixins
from rest_framework.response import Response

from Users.models import Profile
from .serializers import ProfileSerializer, ProfileSettingsSerializer


class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    queryset = Profile.objects.all()


class ProfileSettingsViewSet(viewsets.GenericViewSet, viewsets.mixins.UpdateModelMixin):
    serializer_class = ProfileSettingsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve the profile settings for the current user."""
        return self.request.user.profile


class ProfileSettingsAPIView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = ProfileSettingsSerializer

    def get_object(self):
        return get_object_or_404(Profile, user=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            self.perform_update(serializer)
            return Response(serializer.data)