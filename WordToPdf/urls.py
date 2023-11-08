from django.urls import path
from .views import *
urlpatterns = [
    path('word-to-pdf/',wordToPdfView,name='wordToPdf'),
]
