from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Account
from .serializers import AccountListSerializer
from django.http import Http404
from twitter_clone_api.permissions import IsOwnerOrReadOnly
# Create your views here.


class AccountList(generics.ListAPIView):
    queryset = accounts = Account.objects.all()
    serializer_class = AccountListSerializer


class AccountDetail(APIView):
    # Setting form to update account details
    serializer_class = AccountListSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Account.objects.all()
