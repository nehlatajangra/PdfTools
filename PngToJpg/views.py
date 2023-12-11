from django.shortcuts import render
from PIL import Image
from io import BytesIO
from django.http import HttpResponse
# Create your views here.
def pngToJpgView(request):
    # if request.method=='POST'and request.FILES['png_file']:
    #     uploaded_image=request.FILES['png_file']
    #     png_image=Image.open(uploaded_image)
    #     jpeg_buffer = BytesIO()
    #     png_image = png_image.convert('RGB')
    #     png_image.save(jpeg_buffer, format="JPEG")
    #     response = HttpResponse(jpeg_buffer.getvalue(), content_type="image/jpeg")
    #     response['Content-Disposition'] = f'attachment; filename=converted_image.jpg'
    #     return response
    return render(request,'pngToJpg.html')
