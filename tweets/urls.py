from django.urls import path 
from tweets import views

urlpatterns = [
    path('tweets/', views.TweetList.as_view()),
    path('tweets/<int:pk>/',views.TweetDetail.as_view() ) 
]