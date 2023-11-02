from django.urls import path 
from accounts import views

# Patterns
urlpatterns = [
    path('accounts/', views.AccountList.as_view(), )
]