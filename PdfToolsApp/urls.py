
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('PdfToWord.urls')),
    path('',include('PdfToImage.urls')),
    path('',include('PptToPdf.urls')),
    path('',include('ImageToPdf.urls')),
    path('',include('PngToJpg.urls')),
    path('',include('JpgToPng.urls')),

    
]
