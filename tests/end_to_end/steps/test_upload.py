from pathlib import Path

from django.urls import reverse
from pytest_bdd import scenarios, given, when, then

scenarios('../features/upload.feature')
csv_path = Path(__file__).parent.parent.parent.parent / 'csv' / '2024_1_GLS.csv'


@given('the user navigates to the upload page')
def navigate_to_upload_page(page, live_server):
    url = f"{live_server.live_server_url}{reverse('upload_csv')}"
    page.goto(url)
    assert page.title() == 'Upload CSV'


@when('the user selects a file to upload')
def select_file_to_upload(page):
    page.set_input_files('input[type="file"]', csv_path)


@when('the user submits the form')
def submit_form(page):
    page.click('button[type="submit"]')


@then('the file should be successfully uploaded')
def verify_file_upload(page):
    assert page.is_visible('text="Upload successful"')
