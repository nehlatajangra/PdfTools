from django.shortcuts import render
import fitz 
from django.http import HttpResponse
from PIL import Image

# Create your views here.
def pdfToJpgView(request):
    if request.method == 'POST' and request.FILES['pdf_file']:
        pdf_path =request.FILES['pdf_file']

        # Open the PDF file using PyMuPDF.
        pdf_document = fitz.open(pdf_path)

        # Iterate through the pages of the PDF.
        images = []
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            image = page.get_pixmap()
            images.append(Image.frombytes("RGB", [image.width, image.height], image.samples))

        response = HttpResponse(content_type='image/jpeg')
        images[0].save(response, format='JPEG')

        # Set the filename for download.
        response['Content-Disposition'] = f'attachment; filename="{pdf_path.split("/")[-1]}.jpg"'

        return response
    return render(request,'pdfToJpg.html')
