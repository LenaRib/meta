from django.db import models


class Metod(models.Model):
    name = models.TextField()


class Therapist(models.Model):
    name = models.TextField()
    photo = models.TextField()
    metod = models.ForeignKey("Metod", on_delete=models.SET_NULL, null=True)
