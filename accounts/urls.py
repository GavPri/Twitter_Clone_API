from django.urls import path 
from accounts import views

# Patterns
urlpatterns = [
    path('profiles/', views.AccountList.as_aview(), )
]