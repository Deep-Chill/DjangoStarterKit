from django.shortcuts import render
from django.views import View

# Create your views here.


class HomeView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = {
            'api_urls': {
                # Add your API urls here
            }
        }
        return render(request, self.template_name, context)
