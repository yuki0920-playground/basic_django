from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import TodoModel

class TodoList(ListView):
    template_name = 'list.html'
    model = TodoModel

class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel