from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            "id",
            "uuid",
            "username",
            "last_updated",
            "first_name",
            "last_name",
            "age",
            "records",
            "games",
            "pronouns",
            "region",
            "facts",
            "ImgUrl",
            "extra_data",
            "blog_collection",
            "image_collection",
            "user_settings",
        )
