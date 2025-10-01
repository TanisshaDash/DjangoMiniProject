from django.shortcuts import render
from django.forms import formset_factory
from .forms import GeeksForm

def formset_view(request):
    GeeksFormSet = formset_factory(GeeksForm)
    formset = GeeksFormSet()
    return render(request, "home.html", {'formset': formset})

def formset_view(request):
    GeeksFormSet = formset_factory(GeeksForm, extra=3)
    if request.method == 'POST':
        formset = GeeksFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                print(form.cleaned_data)  # Process form data here
    else:
        formset = GeeksFormSet()

    return render(request, "home.html", {'formset': formset})