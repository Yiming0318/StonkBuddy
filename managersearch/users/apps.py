from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    # The ready() method [Django-doc] is called after the registry is fully loaded. 
    # You thus can then perform some operations you want to perform before the server 
    # starts handling requests. 
    def ready(self):
        import users.signals
    