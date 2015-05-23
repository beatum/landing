# -*- coding: utf-8 -*-

from django.contrib import messages


class MessageMixin(object):
    """
    Adds a message on form submission.
    """
    success_message = ''
    errors_message = ''

    def form_valid(self, form):
        response = super(MessageMixin, self).form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)
        return response

    # TODO: Must be work in Django 1.6
    def form_invalid(self, form):
        response = super(MessageMixin, self).form_invalid(form)
        errors_message = self.get_errors_message(form.errors)
        if errors_message:
            messages.error(self.request, errors_message)
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data

    # TODO: Must be work in Django 1.6
    def get_errors_message(self, errors):
        return self.errors_message % errors