from django.db import models
from django.utils import timezone


class Voetbalspelers(models.Model):
    naam = models.CharField(max_length=100)
    actuele_voetbalclub = models.CharField(max_length=100)
    auteur = models.CharField(max_length=100)
    datum_invoer = models.DateTimeField(default=timezone.now)
    datum_laatste_aanpassing = models.DateTimeField(auto_now=True)

    def publiceer(self):
        self.save()

    def __str__(self):
        return self.naam