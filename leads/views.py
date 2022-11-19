from django.shortcuts import render, redirect, reverse
from django.views.generic import (
    TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
    )
from django.http import HttpResponse
from .models import Lead
from .forms import LeadModelForm


class LandingPageView(TemplateView):
    template_name = "landing.html"


class LeadListView(ListView):
    template_name = "index.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"

class LeadDetailView(DetailView):
    template_name = "details.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


class LeadCreateView(CreateView):
    template_name = "create.html"
    form_class = LeadModelForm

    def get_success_url(self) -> str:
        return reverse("leader:home")

class LeadUpdateView(UpdateView):
    template_name = "update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self) -> str:
        return reverse("leader:home")


class LeadDeleteView(DeleteView):
    template_name = "lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self) -> str:
        return reverse("leader:home")


# def land(request):
#     return render(request, 'landing.html')


# def lead(request):
#     leads =  Lead.objects.all()
    
#     context = {
#        "leads": leads
#     }
#     return render(request, 'index.html', context)

# def details(request, pk):
#     lead = Lead.objects.get(id=pk)
#     context = {
#         'lead': lead
#     }
#     return render(request, 'details.html', context)

# def create(request):
#     form = LeadModelForm()
#     if request.method == 'POST':
#         form = LeadModelForm(request.POST)
#         if  form.is_valid():            
#             form.save()
#             return redirect('/leads')
        
#     context = {
#         'form': form
#     }
#     return render(request, "create.html", context)

# def update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadModelForm(instance=lead)
#     if request.method == "POST":
#         form = LeadModelForm(request.POST, instance=lead)
#         if form.is_valid():
#             form.save()
#             return redirect("/hello")
#     context = {
#         'lead': lead,
#         'form': form
#     }
#     return render(request, 'update.html', context)

# def lead_delete(request, pk):
#     lead = Lead.objects.get(id=pk)
#     lead.delete()
#     return redirect('/leads')



