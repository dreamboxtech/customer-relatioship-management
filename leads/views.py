from django.shortcuts import render

from django.http import HttpResponse
from .models import Lead




def hello(request):
    leads =  Lead.objects.all()
    
    context = {
       "leads": leads
    }
    return render(request, 'index.html', context)

def details(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        'lead': lead
    }
    return render(request, 'details.html', context)

def create(request):
    return render(request, "create.html")