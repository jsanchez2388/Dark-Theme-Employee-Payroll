import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EmployeePayroll.settings')

application = get_asgi_application()

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"