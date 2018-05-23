import os, sys
sys.path.append('/myportfolio/myportfolio')

# add the virtualenv site-packages path to the sys.path
sys.path.append('/v_myportfolio/Lib/site-packages')

# poiting to the project settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myportfolio.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()