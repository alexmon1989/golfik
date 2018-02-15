from django.views.generic.base import TemplateView
from django.http import Http404
from .models import About


class AboutView(TemplateView):
    """Отображает главную страницу."""
    template_name = 'about/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['page_data'] = About.objects.first()
        if not context['page_data']:
            raise Http404("About model does not exist.")
        return context
