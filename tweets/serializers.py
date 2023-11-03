from rest_framework import serializers
from .models import Tweet


# Tweet List Serializer
class TweetListSerializer(serializers.ModelSerializer):
    owner =serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
