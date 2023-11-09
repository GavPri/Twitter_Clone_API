from rest_framework import serializers
from .models import Account
from followers.models import Followers


# Accounts List Serializer
class AccountListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()

    # Check for profile ownership
    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    def get_following_id(self, obj):
        user = self.context["request"].user
        if user.is_authenticated:
            following = Followers.objects.filter(owner=user, followed=obj.owner).first()
            return following.id if following else None
        return None

    class Meta:
        model = Account
        fields = [
            "id",
            "owner",
            "created_at",
            "updated_at",
            "name",
            "content",
            "image",
            "is_owner",
            "following_id",
        ]
