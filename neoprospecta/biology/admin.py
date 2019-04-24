import django_rq
from django.contrib import admin

from neoprospecta.biology.models import Specie, Kingdom, Entry


class KingdomAdmin(admin.ModelAdmin):
    list_display = ('label', )
    search_fields = ('label',)
admin.site.register(Kingdom, KingdomAdmin)

class SpecieAdmin(admin.ModelAdmin):
    list_display = ('label',)
    search_fields = ('label',)

admin.site.register(Specie, SpecieAdmin)

class EntryAdmin(admin.ModelAdmin):
    list_display = ('access_id', 'kingdom')
    search_fields = ('access_id', 'sequence', 'kingdom__label', 'specie__label')

admin.site.register(Entry, EntryAdmin)