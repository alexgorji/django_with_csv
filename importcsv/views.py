from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def upload_csv_file(request):
    return render(request, 'importcsv/upload.html')
