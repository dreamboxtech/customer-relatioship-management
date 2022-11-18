from django.shortcuts import render, redirect

from django.http import HttpResponse
from .models import Lead
from .forms import LeadModelForm




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
    form = LeadModelForm()
    if request.method == 'POST':
        form = LeadModelForm(request.POST)
        if  form.is_valid():            
            form.save()
            return redirect('/hello')
        
    context = {
        'form': form
    }
    return render(request, "create.html", context)

def update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/hello")
    context = {
        'lead': lead,
        'form': form
    }
    return render(request, 'update.html', context)



