from django.db import models

# Create your models here.

class EntryParameter(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False, unique=True)
    url = models.CharField(max_length=500, null=False, blank=False, unique=True)
    row_start = models.IntegerField()
    row_end = models.IntegerField()

    def __str__(self):
        return '{name}'.format(name=self.name)

class PaginationParameter(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False, unique=True)
    rows = models.IntegerField()

    def __str__(self):
        return '{name}'.format(name=self.name)