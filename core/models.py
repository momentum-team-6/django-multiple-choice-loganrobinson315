from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse

class User(AbstractUser):
    pass

class Deck(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='decks')
    def get_absolute_url(self):
        return reverse('deck-detail', args=[str(self.id)])
    
    def __str__(self):
        return self.title


class Card(models.Model):
    question = models.CharField(max_length=2000)
    answer = models.TextField(max_length=5000)
    deck = models.ForeignKey('Deck', on_delete=models.CASCADE, blank=True, null=True, related_name='cards')


    def __str__(self):
        return self.question