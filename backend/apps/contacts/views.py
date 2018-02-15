from django.views.generic.base import TemplateView
from django.http import Http404
from .models import Contact


class ContactView(TemplateView):
    """Отображает страницу Контакты."""
    template_name = 'contacts/contacts.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['page_data'] = Contact.objects.first()
        if not context['page_data']:
            raise Http404("Contact model does not exist.")
        return context
