from django.urls import path
from .views import *
urlpatterns = [

    path('png-to-jpg/',pngToJpgView,name='pngToJpg')
]