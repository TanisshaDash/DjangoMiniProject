# mini/views.py
from django.shortcuts import render, redirect
from .forms import URLForm
from .models import ValidatedURL

def index(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            ValidatedURL.objects.create(url=url)
            return redirect('success')
    else:
        form = URLForm()
    return render(request, "index.html", {'form': form})

def success(request):
    validated_urls = ValidatedURL.objects.all()
    return render(request, "success.html", {'validated_urls': validated_urls})