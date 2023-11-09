from rest_framework import generics, filters
from .models import Account
from .serializers import AccountListSerializer
from twitter_clone_api.permissions import IsOwnerOrReadOnly
from django.db.models import Count
# Create your views here.


class AccountList(generics.ListAPIView):
    queryset = accounts = Account.objects.annotate(
        tweet_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = AccountListSerializer


class AccountDetail(generics.RetrieveUpdateAPIView):
    # Setting form to update account details
    serializer_class = AccountListSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Account.objects.all()
