from rest_framework import serializers
from .models import Tweet
from likes.models import Likes
from django.contrib.humanize.templatetags.humanize import naturaltime


# Tweet List Serializer
class TweetListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    account_id = serializers.ReadOnlyField(source="owner.account.id")
    account_image = serializers.ReadOnlyField(source="owner.account.image.url")
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    replies_count = serializers.ReadOnlyField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_like_id(self, obj):
        user = self.context["request"].user
        if user.is_authenticated:
            like = Likes.objects.filter(owner=user, tweet=obj).first()
            return like.id if like else None
        return None

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    # Code to validate images
    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError("Image size larger than 2MB")
        if value.image.width > 4096:
            raise serializers.ValidationError("Image width is larger than 4096px")
        if value.image.height > 4096:
            raise serializers.ValidationError("Image height is larger than 4096px")
        return value

    # Check for ownership
    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    # Meta Classes
    class Meta:
        model = Tweet
        fields = [
            "id",
            "owner",
            "created_at",
            "updated_at",
            "content",
            "image",
            "is_owner",
            "account_id",
            "account_image",
            "content",
            "like_id",
            "likes_count",
            "replies_count",
        ]
