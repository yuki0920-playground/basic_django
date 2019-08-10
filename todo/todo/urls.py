from django.urls import path
from .views import TodoList

urlpatterns = [
    path('list/', TodoList.as_view()),
    ]
