from django.db import models


class Psychotherapists(models.Model):
    name = models.CharField(max_length=255)
    photo = models.TextField(default="N/A")
    metod = models.TextField(default="N/A")
