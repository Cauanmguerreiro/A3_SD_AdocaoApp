from django.apps import AppConfig


class SocialnetworksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.socialnetworks' # Para consistência com INSTALLED_APPS
    verbose_name = 'Redes Sociais' # Corrigido para 'Redes Sociais' conforme solicitado