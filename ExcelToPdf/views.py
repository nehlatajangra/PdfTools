from django.shortcuts import render

# Create your views here.
def excelToPdfView(request):
    return render(request,'excelToPdf.html')