from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=200, blank=True)
    body = models.TextField(blank=True)
    author = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title