from rest_framework import serializers
from .models import Account


# Accounts List Serializer
class AccountListSerializer(serializers.ModelSerializer):
    owner =serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Account
        fields = '__all__'