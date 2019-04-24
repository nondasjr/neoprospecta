from django.core.management.base import BaseCommand

from util.import_entry import Process


class Command(BaseCommand):
    help = 'Processa all entry'

    def handle(self, *args, **kwargs):
        process = Process()
        process.run()
