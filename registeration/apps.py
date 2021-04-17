from django.apps import AppConfig


class RegisterationConfig(AppConfig):
    name = 'registeration'

    def ready(self):
        import registeration.signals