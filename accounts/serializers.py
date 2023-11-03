from rest_framework import serializers
from .models import Account


# Accounts List Serializer
class AccountListSerializer(serializers.ModelSerializer):
    owner =serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    # Check for profile ownership
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner


    class Meta:
        model = Account
        fields = [
          'id', 'owner', 'created_at', 'updated_at',
          'name', 'content', 'image', 'is_owner'
        ]