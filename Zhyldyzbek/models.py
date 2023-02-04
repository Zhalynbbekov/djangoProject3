from django.db import models


# Create your models here.

class Zagons(models.Model):
    title = models.CharField('Name', max_length=50)

    def __str__(self):
        return self.title


class Sheeps(models.Model):
    title = models.CharField('Sheeps', max_length=50)
    zagon = models.ForeignKey(Zagons, on_delete=models.SET_NULL, null=True, blank=True, related_name='del_zagonsheeps')

    def __str__(self):
        return self.title


class Deleted_sheeps(models.Model):
    title = models.CharField('Sheeps', max_length=50)
    zagon = models.ForeignKey(Zagons, on_delete=models.SET_NULL, null=True, blank=True, related_name='zagonsheeps')

    def __str__(self):
        return self.title
