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
    staticfiles_dir = project_root / 'staticfiles'
    if not staticfiles_dir.exists():
        call_command('collectstatic', '--noinput', '--clear')
except Exception as e:
    print(f"Static files collection failed: {e}")

# Import WSGI application
from Gaurishankar_Jyotishkendra.wsgi import application

# Import Django's static file serving
from django.conf import settings
from django.http import HttpResponse, FileResponse
from django.core.wsgi import get_wsgi_application

# Custom WSGI handler to serve static files
class StaticFilesMiddleware:
    def __init__(self, app):
        self.app = app
        self.static_root = Path(settings.STATIC_ROOT)
        self.static_url = settings.STATIC_URL.rstrip('/')
    
    def __call__(self, environ, start_response):
        path = environ.get('PATH_INFO', '')
        
        # Check if this is a static file request
        if path.startswith(self.static_url):
            file_path = path[len(self.static_url):].lstrip('/')
            static_file = self.static_root / file_path
            
            if static_file.exists() and static_file.is_file():
                try:
                    # Serve the static file
                    response = FileResponse(open(static_file, 'rb'))
                    content_type = self.get_content_type(static_file)
                    
                    def custom_start_response(status, headers, exc_info=None):
                        headers.append(('Content-Type', content_type))
                        headers.append(('Cache-Control', 'public, max-age=31536000'))
                        return start_response(status, headers, exc_info)
                    
                    return response(environ, custom_start_response)
                except Exception as e:
                    print(f"Error serving static file: {e}")
        
        # Pass to Django app
        return self.app(environ, start_response)
    
    def get_content_type(self, file_path):
        suffix = file_path.suffix.lower()
        content_types = {
            '.css': 'text/css',
            '.js': 'application/javascript',
            '.png': 'image/png',
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.gif': 'image/gif',
            '.svg': 'image/svg+xml',
            '.ico': 'image/x-icon',
            '.woff': 'font/woff',
            '.woff2': 'font/woff2',
            '.ttf': 'font/ttf',
            '.eot': 'application/vnd.ms-fontobject',
        }
        return content_types.get(suffix, 'application/octet-stream')

# Wrap the application with static files middleware
app = StaticFilesMiddleware(application)
