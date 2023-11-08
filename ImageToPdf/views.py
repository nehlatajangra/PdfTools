from django.shortcuts import render
import os
import tempfile
from PIL import Image
from django.http import  HttpResponseBadRequest, FileResponse

# Create your views here.
def jpgToPdfView(request):
    pdf_download_link=None
    if request.method=='POST' and request.FILES['img_file']:
        uploaded_file = request.FILES['img_file']
        if not uploaded_file.name.lower().endswith(('.jpg', '.jpeg', '.png')):
            return HttpResponseBadRequest("Invalid file format. Only JPG or PNG files are supported.")
        image=Image.open(uploaded_file)
        print(image,"-----------------")
        with tempfile.TemporaryDirectory() as temp_dir:
            pdf_file_path = os.path.join(temp_dir, 'output.pdf')

        # Convert the image to PDF
            image = image.convert('RGB')
            image.save(pdf_file_path, 'PDF')
    
        pdf_response = FileResponse(open(pdf_file_path, 'rb'), content_type='application/pdf')
        pdf_response['Content-Disposition'] = f'attachment; filename="{uploaded_file.name.replace(".png", ".pdf")}"'
        return pdf_response
    return render(request,'jpgToPdf.html')



def HomePage(request):
    return render(request,'Index.html')
