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

# Collect static files on startup (for Vercel)
try:
    from django.core.management import call_command
    from django.conf import settings
    staticfiles_dir = Path(settings.STATIC_ROOT)
    
    # Only collect if staticfiles directory doesn't exist or is empty
    if not staticfiles_dir.exists() or not list(staticfiles_dir.iterdir()):
        print("Collecting static files...")
        call_command('collectstatic', '--noinput', '--clear')
        print("Static files collected successfully")
except Exception as e:
    print(f"Static files collection failed: {e}")

# Import WSGI application
from Gaurishankar_Jyotishkendra.wsgi import application

# Vercel requires this export
app = application
