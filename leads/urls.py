from django.urls import path
from .views import hello, details, create, update

app_name = 'leads'

urlpatterns = [
    path('', hello),
    path('<int:pk>', details),
    path('create/', create),
    path('<int:pk>/update', update)
]