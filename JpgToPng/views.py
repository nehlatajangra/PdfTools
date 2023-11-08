from django.shortcuts import render
from PIL import Image
from io import BytesIO
from django.http import HttpResponse

# Create your views here.
def jpgToPngView(request):
    if request.method=='POST'and request.FILES['jpg_file']:
        uploaded_image=request.FILES['jpg_file']
        png_image=Image.open(uploaded_image)
        jpeg_buffer = BytesIO()
        png_image = png_image.convert('RGB')
        png_image.save(jpeg_buffer, format="PNG")
        response = HttpResponse(jpeg_buffer.getvalue(), content_type="image/png")
        response['Content-Disposition'] = f'attachment; filename=converted_image.png'
        return response
    return render(request,'jpgToPng.html')