"""
WSGI config for ntkproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ntkproject.settings')

application = get_wsgi_application()

os.environ["SECRET_KEY"] = '67e#6seh6mbr@qfp64_&ejbmu%o75$!gf$mqsjy)0o3w$c6j73'