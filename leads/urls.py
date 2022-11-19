from django.urls import path
from .views import (
    lead, details, create, update, lead_delete,
    LeadListView, LeadDetailView, LeadCreateView,
    LeadUpdateView, LeadDeleteView
    )

app_name = 'leads'


urlpatterns = [
    path('', LeadListView.as_view(), name="home"),
    path('<int:pk>', LeadDetailView.as_view(), name="details"),
    path('create/', LeadCreateView.as_view(), name="create"),
    path('<int:pk>/update', LeadUpdateView.as_view(), name="update"),
    path('<int:pk>/delete', LeadDeleteView.as_view(), name="delete")
]
# function-based view

# urlpatterns = [
#     path('', lead, name="home"),
#     path('<int:pk>', details, name="details"),
#     path('create/', create, name="create"),
#     path('<int:pk>/update', update, name="update"),
#     path('<int:pk>/delete', lead_delete, name="delete")
# ]


