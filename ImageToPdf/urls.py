from django.urls import path
from .views import *
urlpatterns = [
    path('jpg-to-pdf/',jpgToPdfView,name='jpgtoPdf'),
    path('',HomePage,name='homePage')
]