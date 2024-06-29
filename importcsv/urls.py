from django.urls import path
from .views import upload_csv_file

app_name = 'importcsv'

urlpatterns = [
    path('/upload', upload_csv_file, name='upload')
]
