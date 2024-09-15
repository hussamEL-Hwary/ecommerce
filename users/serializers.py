from django.contrib.auth import get_user_model
from rest_framework import serializers

USER_MODEL = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = USER_MODEL
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'is_active', 'is_admin']
        extra_kwargs = {
            'password': {'write_only': True},
            'is_active': {'help_text': 'Can only be set to `true` or `false` on update'}
        }
