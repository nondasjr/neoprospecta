import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'neoprospecta'))
from django.core.wsgi import get_wsgi_application
os.environ['DJANGO_SETTINGS_MODULE'] = 'neoprospecta.settings'
application = get_wsgi_application()

from util.import_entry import Process

process = Process()
process.run()
