import django_rq
from django.contrib import admin
from neoprospecta.parameter.models import EntryParameter, PaginationParameter
# Register your models here.
from util.import_entry import Process, process_entry


def to_process_entry(self, request, queryset):

    queue = django_rq.get_queue()
    queue.enqueue(process_entry)
    self.message_user(request, "A entry será processada em breve")

to_process_entry.short_description = "Processar entries"

class EntryParameterAdmin(admin.ModelAdmin):
    list_display = ('name', 'row_start', 'row_end')
    search_fields = ('name',)
    actions = [to_process_entry]

admin.site.register(EntryParameter, EntryParameterAdmin)

class PaginationParameterAdmin(admin.ModelAdmin):
    list_display = ('name', 'rows' )
    search_fields = ('name',)

admin.site.register(PaginationParameter, PaginationParameterAdmin)