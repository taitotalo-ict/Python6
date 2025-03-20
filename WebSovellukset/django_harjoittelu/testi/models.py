from django.db import models

class EsimerkkiMalli(models.Model):
    nimi = models.CharField(max_length=50)
    luotu = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nimi
    
    class Meta:
        verbose_name_plural = 'Esimerkkimallit'

