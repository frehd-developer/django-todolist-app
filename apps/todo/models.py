from django.db import models


class Todo(models.Model):
    description = models.CharField(max_length=255)
    state = models.CharField(max_length=20)
