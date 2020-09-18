from django.conf import settings
from django.db import models
from django.utils import timezone

class Todolist(models.Model):
    genre = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)