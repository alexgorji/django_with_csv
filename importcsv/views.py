from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def upload_csv_file(request):
    if request.method == 'GET':
        return render(request, 'importcsv/import_csv.html')
    elif request.method == 'POST':
        print(request.FILES["file"])
        return render(request, 'importcsv/import_csv.html', context={'success_message': 'Upload was successful'})
