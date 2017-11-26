from django.apps import AppConfig


class SignaldetectConfig(AppConfig):
    name = 'signaldetect'
    def ready(self):
        import signaldetect.signals
