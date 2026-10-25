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

# Run migrations for in-memory database
from django.core.management import call_command
try:
    call_command('migrate', '--run-syncdb', verbosity=0)
except Exception as e:
    pass  # Ignore migration errors

# Import WSGI application
from Gaurishankar_Jyotishkendra.wsgi import application

# Vercel requires this export
app = application
