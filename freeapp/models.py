from django.db import models

# Create your models here.


class regmodel(models.Model):
    catchchoice = [
        ('Kerala', 'Kerala'),
        ('TamilNadu', 'TamilNadu'),
        ('Karnataka', 'Karnataka'),
        ('Maharashtra', 'Maharashtra')
    ]
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    gender = models.CharField(max_length=20)
    state = models.CharField(max_length=30, choices=catchchoice)