
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('PdfToWord.urls')),
    path('',include('PdfToImage.urls')),
    path('',include('PptToPdf.urls')),
    path('',include('ImageToPdf.urls')),
    path('',include('PngToJpg.urls')),
    path('',include('JpgToPng.urls')),
    path('',include('WordToPdf.urls')),
    path('',include('ExcelToPdf.urls'))

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
