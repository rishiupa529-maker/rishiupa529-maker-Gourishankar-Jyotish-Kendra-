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

# Collect static files on Vercel deployment
from django.core.management import call_command
from django.conf import settings

if os.getenv('VERCEL'):
    try:
        call_command('collectstatic', '--noinput', '--clear')
        print("Static files collected successfully")
    except Exception as e:
        print(f"Error collecting static files: {e}")

# Import WSGI application
from Gaurishankar_Jyotishkendra.wsgi import application

# Vercel requires this export
app = application
