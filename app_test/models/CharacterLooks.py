from django.db import models

class CharacterLooks(models.Model):
    CHARACTER_CD = models.CharField(max_length=8)
    CHARACTER_HEIGHT = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)
    CHARACTER_WEIGHT = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)

    def __str__(self):
      return str(self.CHARACTER_CD)
