from rest_framework import serializers
from .models import Tweet


# Tweet List Serializer
class TweetListSerializer(serializers.ModelSerializer):
    owner =serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')



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