from django.urls import path
from .views import *
urlpatterns = [
    path('pdf-to-jpg/',pdfToJpgView,name='pdfToJpg')
]