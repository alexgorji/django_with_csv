from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def upload_csv(request):
    HttpResponse(
        'This site will be used to upload a csv file. This file will be then to json format und be shown as a editable form. You will be able to make changes, select rows and colums and save the result into a json data.')
