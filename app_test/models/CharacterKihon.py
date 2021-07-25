from django.db import models

class CharacterKihon(models.Model):
    CHARACTER_CD = models.CharField(max_length=8)
    CHARACTER_NAME = models.CharField(max_length=30)
    CHARACTER_KIND = models.CharField(max_length=2)
    CHARACTER_BIRTH = models.DateField()

    def __str__(self):
      return str(self.CHARACTER_CD)
