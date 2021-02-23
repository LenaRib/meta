from django.db import models


class Psychotherapists(models.Model):
    id = models.CharField(primary_key=True, max_length=18)
    name = models.CharField(max_length=255)
    photo = models.TextField(default="N/A")
    metod = models.TextField(default="N/A")


class Log(models.Model):
    log_date = models.TimeField(auto_now=False, auto_now_add=True)
    event = models.TextField(default="N/A")
