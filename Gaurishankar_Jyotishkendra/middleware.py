from django.http import HttpResponse
from django.db import OperationalError
import logging

logger = logging.getLogger(__name__)


class DatabaseErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
            return response
        except OperationalError as e:
            logger.error(f"Database connection error: {e}")
            # Return a friendly error page
            return HttpResponse(
                """
                <html>
                <head>
                    <title>Database Connection Error</title>
                    <style>
                        body {
                            font-family: Arial, sans-serif;
                            display: flex;
                            justify-content: center;
                            align-items: center;
                            height: 100vh;
                            margin: 0;
                            background: #120904;
                            color: #f4ce6a;
                        }
                        .error-container {
                            text-align: center;
                            padding: 40px;
                            background: #221108;
                            border: 1px solid #d4af37;
                            border-radius: 15px;
                            max-width: 500px;
                        }
                        h1 { margin-top: 0; }
                        .btn {
                            display: inline-block;
                            margin-top: 20px;
                            padding: 10px 20px;
                            background: #f4ce6a;
                            color: #1a0c02;
                            text-decoration: none;
                            border-radius: 5px;
                        }
                    </style>
                </head>
                <body>
                    <div class="error-container">
                        <h1>Database Connection Error</h1>
                        <p>We're experiencing database connectivity issues. Please try again later.</p>
                        <a href="/" class="btn">Return to Home</a>
                    </div>
                </body>
                </html>
                """,
                status=503
            )
