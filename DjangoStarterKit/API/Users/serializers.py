from rest_framework import serializers
from Users.models import Profile
from django.contrib.auth.models import User
from datetime import date


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'full_name']
        read_only_fields = ['id', 'username', 'full_name']

    def get_full_name(self, obj):
        return obj.get_full_name()


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ('user', 'id', 'slug', 'created_at')


class ProfileSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('bio', 'picture',)