from django.db import models

# Create your models here.

class SobreNos(models.Model):
    missao = models.TextField(blank=True, null=True)
    visao = models.TextField(blank=True, null=True)
    valores = models.TextField(blank=True, null=True)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

    class Meta:
        verbose_name = 'Sobre Nós'
        verbose_name_plural = 'Sobre Nós'