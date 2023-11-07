from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Tweet
from .serializers import TweetListSerializer

# Create your views here.

class TweetList(APIView):
    def get(self, request):
        tweets = Tweet.objects.all()
        serializer = TweetListSerializer(
            tweets, many=True, context={'request':request}
        )
        return Response(serializer.data)