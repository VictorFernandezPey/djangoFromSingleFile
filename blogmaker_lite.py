from django.conf import settings
from django.http import HttpResponse
from django.urls import path
from django.core.handlers.wsgi import WSGIHandler
from django.core.management import \
    execute_from_command_line
from django.urls import path
from pathlib import Path
import os
import django
from django.shortcuts import render

'''
settings.configure(
    ROOT_URLCONF=__name__,
    DEBUG=True,
    SECRET_KEY="my-secret-key",
    TEMPLATES=[
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [Path(__file__).parent / "templates"],
        }
    ],
)
'''
# Lo anterior de settings.configure se reemplaza por lo siguiente para usar los archivos de la carpeta templates
# Load settings.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

def index(request):
    return render(request, "index.html")

urlpatterns = [
    path("", index)
]

application = WSGIHandler()

if __name__ == "__main__":
    execute_from_command_line()