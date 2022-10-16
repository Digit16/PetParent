from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    # category = models.Choices()
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_private_person = models.BooleanField()
    date_posted = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return f'{self.title}'
