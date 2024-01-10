from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class SettingsView(LoginRequiredMixin, TemplateView):
    template_name = 'Users/settings.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
