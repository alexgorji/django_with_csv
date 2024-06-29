from pathlib import Path

from django.urls import reverse
from pytest_bdd import scenarios, given, when, then

from tests.end_to_end.page_objects.upload_csv import UploadCSVPage

scenarios('../features/upload.feature')
csv_path = Path(__file__).parent.parent.parent.parent / 'data' / '2024_1_GLS.csv'


@given('the user navigates to the upload page')
def navigate_to_upload_page(page, live_server):
    print('navigate_to_upload_page')
    upload_page = UploadCSVPage(page)
    url = f"{live_server.live_server_url}{reverse('importcsv:upload')}"
    upload_page.navigate(url)
    assert page.title() == 'Upload CSV'


@when('the user selects a file to upload')
def select_file_to_upload(page):
    print('select_file_to_upload')
    upload_page = UploadCSVPage(page)
    print(csv_path)
    upload_page.upload_file(csv_path)


@when('the user submits the form')
def submit_form(page):
    print('submit_form')
    upload_page = UploadCSVPage(page)
    upload_page.click_submit_button()


@then('the file should be successfully uploaded')
def verify_file_upload(page):
    print('verify_file_upload')
    upload_page = UploadCSVPage(page)
    assert upload_page.get_success_message() == 'Upload successful'
