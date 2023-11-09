from rest_framework import generics, permissions, filters
from .models import Tweet
from .serializers import TweetListSerializer
from twitter_clone_api.permissions import IsOwnerOrReadOnly
from django.db.models import Count


# Create your views here.
class TweetList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = TweetListSerializer
    queryset = Tweet.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.user.request)


class TweetDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = TweetListSerializer
    queryset = Tweet.objects.all()
