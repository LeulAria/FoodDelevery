"""Collection serializers."""
from typing import Any, Dict

from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers


class UserDetailsSerializer(serializers.Serializer):
    """User detail serializer."""

    email = serializers.EmailField(read_only=True)

    username = serializers.CharField(read_only=True)

    picture = serializers.ImageField(read_only=True)
    
    phone_number = serializers.ImageField(read_only=True)

    is_active = serializers.BooleanField(read_only=True)


class JWTSerializer(serializers.Serializer):
    """JWT serializer."""

    access_token = serializers.CharField(read_only=True)

    refresh_token = serializers.CharField(read_only=True)

    user = UserDetailsSerializer(read_only=True)


class CustomRegisterSerializer(RegisterSerializer):
    """Custom Register serializer."""

    picture = serializers.ImageField(required=False)

    full_name = serializers.CharField(max_length=300)

    phone_number = serializers.CharField(max_length=300) 

    def get_cleaned_data(self: "CustomRegisterSerializer") -> Dict[str, Any]:
        """Cleaning for input data."""
        data_dict = super().get_cleaned_data()
        data_dict["picture"] = self.validated_data.get(
            "picture", "images/default/pic.png"
        )
        data_dict["full_name"] = self.validated_data.get("full_name", "")
        data_dict["phone_number"] = self.validated_data.get("phone_number", "")

        return data_dict
