from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Tweet
from .serializers import TweetListSerializer
from django.http import Http404


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