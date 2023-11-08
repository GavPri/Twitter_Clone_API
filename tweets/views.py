from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Tweet
from .serializers import TweetListSerializer
from django.http import Http404
from twitter_clone_api.permissions import IsOwnerOrReadOnly


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
