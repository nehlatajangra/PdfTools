from django.urls import path
from .views import *

urlpatterns = [
    path('pdf-to-word/',pdfToWordView,name='pdfToWord'),
]