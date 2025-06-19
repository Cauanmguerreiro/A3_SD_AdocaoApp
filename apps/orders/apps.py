from django.apps import AppConfig


class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.orders' # Para consistência com INSTALLED_APPS
    verbose_name = 'Pedidos'