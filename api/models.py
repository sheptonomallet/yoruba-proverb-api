from django.db import models

# Create your models here.

class Proverb(models.Model):
    yoruba = models.CharField(max_length=700)
    english = models.CharField(max_length=700)
    wisdom = models.CharField(max_length=700)

    def __str__(self):
        return self.yoruba 