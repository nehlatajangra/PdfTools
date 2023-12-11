from django.urls import path
from .views import *
urlpatterns = [

    path('jpg-to-png/',jpgToPngView,name='jpgToPng')
]