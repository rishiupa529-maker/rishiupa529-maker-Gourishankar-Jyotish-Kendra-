import os
import sys
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Gaurishankar_Jyotishkendra.settings')

# Import Django and initialize
import django
django.setup()

# Import WSGI application
from Gaurishankar_Jyotishkendra.wsgi import application

# Vercel requires this export
app = application

# Collect static files for Vercel
from django.core.management import call_command
from django.conf import settings

if not os.path.exists(settings.STATIC_ROOT):
    os.makedirs(settings.STATIC_ROOT, exist_ok=True)
    try:
        call_command('collectstatic', '--noinput', verbosity=0)
    except Exception as e:
        print(f"Collectstatic warning: {e}")
