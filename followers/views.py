from rest_framework import generics, permissions
from twitter_clone_api.permissions import IsOwnerOrReadOnly
from .models import Followers
from .serializers import FollowerSerializer

# Create your views here.


class FollowersList(generics.ListCreateAPIView):
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Followers.objects.all()
