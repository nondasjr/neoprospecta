from django.shortcuts import render

# Create your views here.
from django.template import loader
from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny

from neoprospecta.biology.models import Entry
from neoprospecta.biology.serializers import EntrySerializer
from neoprospecta.parameter.models import PaginationParameter


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = (AllowAny,)
    filter_backends = (filters.SearchFilter,)

    search_fields = ('access_id',
                     'sequence',
                     'kingdom__label',
                     'specie__label'
                     )

def index(request, page=1):
    init, end = paginate(page)
    entries = Entry.objects.all()[init:end]

    context = {
        'entries': entries, 'pages':range(0,pages())
    }
    return render(request, 'index.html', context)

def paginate(page):
    init = 0
    param = PaginationParameter.objects.last()
    rows = param.rows if param else 1000
    if page > 1:
        init = (page - 1) * rows

    return init, init + rows


def pages():
    param = PaginationParameter.objects.last()
    rows = param.rows if param else 1000
    entries_length = Entry.objects.count()

    if entries_length <= rows:
        pages = 1
    else:
        pages = int(entries_length / rows)
        pages = pages + 1 if (entries_length % rows) > 0 else pages

    return pages