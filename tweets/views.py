from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Tweet
from .serializers import TweetListSerializer
from django.http import Http404
from twitter_clone_api.permissions import IsOwnerOrReadOnly


# Create your views here.

class TweetList(APIView):
    # For user form.
    serializer_class = TweetListSerializer
    # Permissions 
    permission_classes  = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    def get(self, request):
        tweets = Tweet.objects.all()
        serializer = TweetListSerializer(
            tweets, many=True, context={'request':request}
        )
        return Response(serializer.data)

    def post(self, request):
        # Deserialize the data.
        serializer = TweetListSerializer(
            data = request.data, context = {'request': request}
        )
        # If data is valid.
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # If data is invalid.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TweetDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = TweetListSerializer
    
    # Get tweet by ID
    def get_object(self, pk):
        try:
            tweet = Tweet.objects.get(pk=pk)
            self.check_object_permissions(self.request, tweet)
            return tweet
        except Tweet.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        tweet = self.get_object(pk)
        serializer = TweetListSerializer(
            tweet, context={'request':request})
        return Response(serializer.data)

    # Edit tweets/put method
    def put(self, request, pk):
        tweet = self.get_object(pk)
        serializer = TweetListSerializer(tweet, data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    # Delete Method.
    def delete(self, request, pk):
        tweet = self.get_object(pk)
        tweet.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
