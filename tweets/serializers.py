from rest_framework import serializers
from .models import Tweet


# Tweet List Serializer
class TweetListSerializer(serializers.ModelSerializer):
    owner =serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    # Code to validate images
    def validate_image(self, value):
      if value.size > 1024 * 1024 * 2:
        raise serializers.ValidationError(
          'Image size larger than 2MB'
        )
      if value.image.width > 4096:
        raise serializers.ValidationError(
          'Image width is larger than 4096px'
        )
      if value.image.height > 4096:
        raise serializers.ValidationError(
          'Image height is larger than 4096px'
        )
      return value

    # Check for ownership
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    # Meta Classes 
    class Meta:
        model = Account
        fields = [
          'id', 'owner', 'created_at', 'updated_at',
          'content', 'image', 'is_owner',
          'profile_id', 'profile_image', 'content',
        ]