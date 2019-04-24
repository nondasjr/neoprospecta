import uuid

from django.db import models

# Create your models here.
class Kingdom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.CharField(max_length=150, null=False, blank=False, unique=True)

    def __str__(self):
        return '{label}'.format(label=self.label)


class Specie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.CharField(max_length=150, null=False, blank=False, unique=True)

    def __str__(self):
        return '{label}'.format(label=self.label)


class Entry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    access_id = models.CharField(unique=True, null=False, blank=False, max_length=19)
    sequence = models.CharField(null=True, blank=False, max_length=80)
    kingdom = models.ForeignKey(Kingdom, related_name='entry', on_delete=models.CASCADE, blank=True)
    specie = models.ManyToManyField(Specie, related_name='entry')

    def __str__(self):
        return '{access_id} - {kingdom}'.format(access_id=self.access_id, kingdom=self.kingdom)
