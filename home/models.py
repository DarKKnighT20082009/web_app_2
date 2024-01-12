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


class User(models.Model):
    name = models.CharField(max_length=50, null=False)
    surname = models.CharField(max_length=50, null=False)
    gender = models.CharField(max_length=10 ,null=False)
    hobby = models.CharField(max_length=100, null=False)
    birthday = models.DateField(null=False)
    age = models.IntegerField(null=False)

    def __str__(self):
        return f"{self.name} {self.surname}"
