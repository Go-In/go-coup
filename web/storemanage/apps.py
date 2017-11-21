from django.apps import AppConfig


class StoremanageConfig(AppConfig):
    name = 'storemanage'

    def ready(self):
        import storemanage.signals
