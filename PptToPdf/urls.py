from django.urls import path
from .views import *
urlpatterns = [

    path('ppt-to-pdf/',pptToPdfView,name='pptToPdf')
]