from django.db import models

class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()