from django.apps import AppConfig


class DeliveryCompanyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'delivery_company'

    def ready(self):
        from .jobs import updater
        updater.start()
