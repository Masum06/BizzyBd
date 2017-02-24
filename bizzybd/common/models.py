from django.db import models
from django.contrib.auth.models import User


class Website(models.Model):

    name = models.CharField(max_length=50, unique=True)
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.name


class Div(models.Model):

    name = models.TextField()

    def __str__(self):
        return self.name