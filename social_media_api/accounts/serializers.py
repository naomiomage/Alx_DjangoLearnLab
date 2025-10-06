from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        # Create the user securely (hashing password)
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )

        # Create authentication token for the user
        Token.objects.create(user=user)
        return user
