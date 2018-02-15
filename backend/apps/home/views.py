from django.views.generic.base import TemplateView
from django.http import Http404
from .models import Home


class HomeView(TemplateView):
    """Отображает главную страницу."""
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['article'] = Home.objects.first()
        if not context['article']:
            raise Http404("Home model does not exist.")
        return context
