from rest_framework import generics, permissions, filters
from .models import Tweet
from .serializers import TweetListSerializer
from twitter_clone_api.permissions import IsOwnerOrReadOnly
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class TweetList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = TweetListSerializer
    queryset = Tweet.objects.annotate(
        likes_count=Count("likes", distinct=True),
        replies_count=Count("replies", distinct=True),
    ).order_by("-created_at")
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        # user feed
        "owner__followed__owner__account",
        # user liked post
        "likes__owner__account",
        # user profile
        "owner__account",
    ]
    ordering_fields = [
        "likes_count",
        "replies_count",
        "likes__created_at",
        "replies__created_at",
    ]

    search_fields = ["owner__username", "content"]

    def perform_create(self, serializer):
        serializer.save(owner=self.user.request)


class TweetDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = TweetListSerializer
    queryset = Tweet.objects.annotate(
        likes_count=Count("likes", distinct=True),
        replies_count=Count("replies", distinct=True),
    ).order_by("-created_at")
