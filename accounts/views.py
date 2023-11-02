from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Account
from .serializers import AccountListSerializer
from django.http import Http404
# Create your views here.


class AccountList(APIView):
    # Get request to view account list. 
    def get(self, request):
        accounts = Account.objects.all()
        # Serializer instance 
        serializer = AccountListSerializer(accounts, many=True)
        return Response(serializer.data)


class AccountDetail(APIView):
    # Function to handle request for account that does not exists.
    def get_object(self, pk):
        try:
            account = Account.objects.get(pk=pk)
            return account
        except Account.DoesNotExist:
            raise Http404

    # Function to return account by id
    def get(self, request, pk):
        account = self.get_object(pk)
        serializer = AccountListSerializer(account)
        return Response(serializer.data)