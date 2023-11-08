from rest_framework import generics, permissions
from twitter_clone_api.permissions import IsOwnerOrReadOnly
from likes.models import Likes
from likes.serializers import LikeSerializer


class LikeList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Likes.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
