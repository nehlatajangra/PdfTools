from django.shortcuts import render
from django.http import HttpResponse
from pdf2docx import Converter
from django.core.files.storage import FileSystemStorage

# Create your views here.
def pdfToWordView(request):
    if request.method == 'POST' and request.FILES.get('pdf_file'):
        pdf_file = request.FILES['pdf_file']
        fs = FileSystemStorage()
        pdf_filename = fs.save(pdf_file.name, pdf_file)
        docx_filename = pdf_filename.replace('.pdf', '.docx')
        converter = Converter(pdf_filename)
        converter.convert(docx_filename, start=0, end=None)
        with open(docx_filename, 'rb') as docx_file:
            response = HttpResponse(docx_file.read(), content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
            response['Content-Disposition'] = f'attachment; filename={docx_filename}'
        return response
    return render(request, 'pdfToWord.html')

