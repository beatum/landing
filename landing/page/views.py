# from django.shortcuts import render

from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy
# from django.utils.translation import ugettext_lazy as _

from landing.page.forms import PersonForm
from landing.core.mixin import MessageMixin


class IndexView(MessageMixin, FormView):
    form_class = PersonForm
    template_name = "page/index.html"
    success_url = reverse_lazy('index')
    success_message = 'done'
    errors_message = 'error'

    def form_valid(self, form):
        form.save()
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        return super(IndexView, self).form_valid(form)


# from django.views.generic.base import TemplateView
#
# class IndexView(TemplateView):
#     template_name = "page/index.html"
#
#     def get_context_data(self, **kwargs):
#         context = super(IndexView, self).get_context_data(**kwargs)
#         return context

