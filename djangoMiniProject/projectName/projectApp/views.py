from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import GeeksForm
from .models import GeeksModel

class GeeksFormView(FormView):
    template_name = "geeks_form.html"     # your template
    form_class = GeeksForm
    success_url = reverse_lazy('success') # redirect after submit

    def form_valid(self, form):
        # save to database
        form.save()
        return super().form_valid(form)

from django.views.generic import TemplateView

class SuccessView(TemplateView):
    template_name = "success.html"