from django.urls import path
from .views import upload, files

urlpatterns = [
    path('upload/', upload),
    path('files/', files),
]
