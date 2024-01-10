from django.db import models
from django.db.models import Model


# Create your models here.
class Vazifa(models.Model):
    nomi = models.CharField(max_length=50, null=False)
    tavsif = models.TextField(null=True)
    oxirgi_muddat = models.DateField()

    def __str__(self):
        return f"{self.nomi} {self.oxirgi_muddat}"

    class Meta:
        verbose_name = 'Vazifa'
        verbose_name_plural = 'Vazifalar'
