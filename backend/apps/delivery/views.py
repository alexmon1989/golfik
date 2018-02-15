from django.views.generic.base import TemplateView
from django.http import Http404
from .models import Delivery


class DeliveryView(TemplateView):
    """Отображает главную страницу."""
    template_name = 'delivery/delivery.html'

    def get_context_data(self, **kwargs):
        context = super(DeliveryView, self).get_context_data(**kwargs)
        context['page_data'] = Delivery.objects.first()
        if not context['page_data']:
            raise Http404("Delivery model does not exist.")
        return context
