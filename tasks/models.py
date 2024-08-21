from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.CharField(max_length=200)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)