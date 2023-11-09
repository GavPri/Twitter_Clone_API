from rest_framework import generics, permissions, filters
from .models import Tweet
from .serializers import TweetListSerializer
from twitter_clone_api.permissions import IsOwnerOrReadOnly
from django.db.models import Count


# Create your views here.
class TweetList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = TweetListSerializer
    queryset = Tweet.objects.annotate(
        likes_count=Count("likes", distinct=True),
        replies_count=Count("replies", distinct=True),
    ).order_by("-created_at")
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        "likes_count",
        "replies_count",
        "likes__created_at",
        "replies__created_at",
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.user.request)


class TweetDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = TweetListSerializer
    queryset = Tweet.objects.annotate(
        likes_count=Count("likes", distinct=True),
        replies_count=Count("replies", distinct=True),
    ).order_by("-created_at")
