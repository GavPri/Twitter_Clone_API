from rest_framework import generics, permissions
from twitter_clone_api.permissions import IsOwnerOrReadOnly
from .models import Replies
from .serializers import RepliesSerializer, RepliesDetailSerializers
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class ReplyList(generics.ListCreateAPIView):
    serializer_class = RepliesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Replies.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["tweet"]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReplyDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = RepliesDetailSerializers
    queryset = Replies.objects.all()
