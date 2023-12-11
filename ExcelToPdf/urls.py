from django.urls import path
from .views import *
urlpatterns = [
    path('excel-to-pdf/',excelToPdfView,name='excelToPdf'),
]