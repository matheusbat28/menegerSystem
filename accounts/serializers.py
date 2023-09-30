from djoser.serializers import UserSerializer
from rest_framework import serializers
from .models import Users

class UserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = Users
        fields = ('first_name', 'last_name', 'email', 'username', 'is_active', 'groups', 'user_permissions')

