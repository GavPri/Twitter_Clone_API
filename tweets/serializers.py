from rest_framework import serializers
from .models import Tweet
from likes.models import Likes


# Tweet List Serializer
class TweetListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    replies_count = serializers.ReadOnlyField()

    def get_like_id(self, obj):
        user = self.context["request"].user
        if user.is_authenticated:
            like = Likes.objects.filter(owner=user, tweet=obj).first()
            return like.id if like else None
        return None

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
            "content",
            "image",
            "is_owner",
            "profile_id",
            "profile_image",
            "content",
            "like_id",
            "likes_count",
            "replies_count",
        ]
