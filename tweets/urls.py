from django.urls import path 
from tweets import views

urlpatterns = [
    path('tweets/', views.TweetList.as_view()), 
]