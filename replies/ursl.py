from django.urls import path
from replies import views

urlpatterns = [
    path('replies/', views.ReplyList.as_view()),
]