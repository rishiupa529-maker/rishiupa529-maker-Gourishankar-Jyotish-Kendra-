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
try:
    django.setup()
except Exception as e:
    print(f"Django setup failed: {e}")
    import traceback
    traceback.print_exc()

# Import WSGI application
try:
    from Gaurishankar_Jyotishkendra.wsgi import application
    app = application
except Exception as e:
    print(f"Failed to import WSGI application: {e}")
    import traceback
    traceback.print_exc()
    # Fallback simple WSGI app
    def simple_app(environ, start_response):
        status = '200 OK'
        response_body = b'Django failed to load. Check logs.'
        response_headers = [
            ('Content-Type', 'text/plain'),
            ('Content-Length', str(len(response_body)))
        ]
        start_response(status, response_headers)
        return [response_body]
    app = simple_app
