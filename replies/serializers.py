from rest_framework import serializers
from replies.models import Replies

class RepliesSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    
    # Check for ownership
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    # Meta Classes
    class Meta:
        model = Replies
        fields = [
            'id', 'owner', 'created_at',
            'content', 'image', 'is_owner',
            'profile_id', 'profile_image', 'content',
        ]


class RepliesDetailSerializers(RepliesSerializer):
    tweet = serializers.ReadOnlyField(source='tweet.id')