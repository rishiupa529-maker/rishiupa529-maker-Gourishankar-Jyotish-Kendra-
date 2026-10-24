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

# Run migrations on Vercel for in-memory database
if os.getenv('VERCEL'):
    from django.core.management import call_command
    try:
        # Run migrations silently
        call_command('migrate', '--run-syncdb', verbosity=0)
        print("Migrations completed successfully")
    except Exception as e:
        print(f"Migration error (non-critical): {e}")

# Import WSGI application
from Gaurishankar_Jyotishkendra.wsgi import application

# Vercel requires this export
app = application
