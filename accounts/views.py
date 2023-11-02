from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Account
# Create your views here.


# Get request to view account list. 
class AccountList(APIView):
    def get(self, request):
        accounts = Account.objects.all()
        return Response(accounts)