from django.shortcuts import render

# relative import of forms
from .models import GeeksModel


def list_view(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}

    # add the dictionary during initialization
    context["dataset"] = GeeksModel.objects.all()
        
    return render(request, "list_view.html", context)