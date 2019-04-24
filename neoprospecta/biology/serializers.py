# coding=utf-8
from django.contrib.auth import get_user_model
from rest_framework import serializers
from neoprospecta.biology.models import Specie, Kingdom, Entry


class KingdomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kingdom
        fields = ('__all__')

class SpecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specie
        fields = ('__all__')

class EntrySerializer(serializers.ModelSerializer):
    specie = SpecieSerializer(required=False, many=True)
    kingdom = KingdomSerializer(required=False, many=False)

    class Meta:
        model = Entry
        fields = ('id', 'access_id', 'sequence', 'kingdom', 'specie')
