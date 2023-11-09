from rest_framework import generics
from rest_framework.views import APIView
from .models import Account
from .serializers import AccountListSerializer
from twitter_clone_api.permissions import IsOwnerOrReadOnly
# Create your views here.


class AccountList(generics.ListAPIView):
    queryset = accounts = Account.objects.all()
    serializer_class = AccountListSerializer


class AccountDetail(generics.RetrieveUpdateAPIView):
    # Setting form to update account details
    serializer_class = AccountListSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Account.objects.all()
