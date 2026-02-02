import re
from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        validators=[]
    )

    class Meta:
        model = User
        fields = ['username', 'password']

    def validate_password(self, value):
        if not re.search(r'[!@#$%^&*]', value):
            raise serializers.ValidationError(
                "Password must contain a special character"
            )
        return value

    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])  # bcrypt happens here
        user.save()
        return user
