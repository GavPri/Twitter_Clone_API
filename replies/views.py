from rest_framework import generics, permissions
from twitter_clone_api.permissions import IsOwnerOrReadOnly
from .models import Replies
from .serializers import RepliesSerializer, RepliesDetailSerializers

# Create your views here.

class ReplyList(generics.ListCreateAPIView):
    serializer_class = RepliesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Replies.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)