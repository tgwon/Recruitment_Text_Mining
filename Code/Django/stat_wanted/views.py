from django.views.generic.base import TemplateView


class Home(TemplateView):
    template_name = 'home.html'

class Introduce(TemplateView):
    template_name = 'introduce.html'
