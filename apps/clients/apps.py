from django.apps import AppConfig


class ClientsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.clients' # Para consistência com INSTALLED_APPS
    verbose_name = 'Clientes'
