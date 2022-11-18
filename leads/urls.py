from django.urls import path
from .views import lead, details, create, update, lead_delete

app_name = 'leads'

urlpatterns = [
    path('', lead, name="home"),
    path('<int:pk>', details, name="details"),
    path('create/', create, name="create"),
    path('<int:pk>/update', update, name="update"),
    path('<int:pk>/delete', lead_delete, name="delete")
]