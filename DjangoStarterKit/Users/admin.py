from django.apps import apps
from django.contrib import admin

# Get all models in the app
app_models = apps.get_app_config('Users').get_models()

# Register each model with the admin
for model in app_models:
    admin.site.register(model)
