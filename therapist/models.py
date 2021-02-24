from django.db import models


class Psychotherapists(models.Model):
    id = models.CharField(primary_key=True, max_length=18)
    name = models.CharField(max_length=255)
    photo = models.TextField()
    # todo method = new model with many to many relations
    metod = models.TextField()


class Log(models.Model):
    log_date = models.TimeField(auto_now=False, auto_now_add=True)
    event = models.TextField()
