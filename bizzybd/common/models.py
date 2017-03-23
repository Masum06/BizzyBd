from django.db import models
from django.contrib.auth.models import User


class Website(models.Model):

    name = models.CharField(max_length=50, unique=True)
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.name


class Div(models.Model):

    website = models.ForeignKey(Website, blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="slim/", blank=True, null=True)
    file = models.FileField(upload_to='filepicker/', blank=True, null=True)

    def __str__(self):
        return self.name
