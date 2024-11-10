import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from email_reader.mail.consumers import MailConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'email_reader.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('ws/mail/', MailConsumer.as_asgi()),
        ])
    ),
})