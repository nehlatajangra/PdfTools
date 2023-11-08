from django.shortcuts import render
from docx2pdf import convert
import tempfile
from django.http import HttpResponseBadRequest, FileResponse
# Create your views here.
def wordToPdfView(request):
    pdf_download_link = None

    if request.method == 'POST' and request.FILES['docx_file']:
        uploaded_file = request.FILES['docx_file']

        if not uploaded_file.name.endswith('.docx'):
            return HttpResponseBadRequest("Invalid file format. Only DOCX files are supported.")

        with tempfile.NamedTemporaryFile(delete=False, suffix='.docx') as temp_file:
            for chunk in uploaded_file.chunks():
                temp_file.write(chunk)

        temp_pdf_file = temp_file.name.replace('.docx', '.pdf')
        convert(temp_file.name, temp_pdf_file)

        pdf_response = FileResponse(open(temp_pdf_file, 'rb'), content_type='application/pdf')

        pdf_response['Content-Disposition'] = f'attachment; filename="{uploaded_file.name.replace(".docx", ".pdf")}"'

        return pdf_response
    
    return render(request,'wordToPdf.html')