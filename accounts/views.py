from rest_framework import generics, filters
from .models import Account
from .serializers import AccountListSerializer
from twitter_clone_api.permissions import IsOwnerOrReadOnly
from django.db.models import Count
# Create your views here.


class AccountList(generics.ListAPIView):
    queryset = accounts = Account.objects.annotate(
        tweet_count=Count("owner__tweet", distinct=True),
        followers_count=Count("owner__followed", distinct=True),
        following_count=Count("owner__following", distinct=True),
    ).order_by("-created_at")
    serializer_class = AccountListSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        "tweet_count",
        "followers_count",
        "following_count",
        "owner__following__created_at",
        "owner__followed__created_at",
    ]


class AccountDetail(generics.RetrieveUpdateAPIView):
    # Setting form to update account details
    serializer_class = AccountListSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = accounts = Account.objects.annotate(
        tweet_count=Count("owner__tweet", distinct=True),
        followers_count=Count("owner__followed", distinct=True),
        following_count=Count("owner__following", distinct=True),
    ).order_by("-created_at")
