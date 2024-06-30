import pytest
from playwright.sync_api import sync_playwright
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.conf import settings


@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }


# @pytest.fixture(autouse=True, scope='function')
# def enable_db_access(transactional_db):
#     pass


@pytest.fixture(autouse=True, scope='function')
def configure_settings(settings):
    settings.DEBUG = True


@pytest.fixture(scope='session')
def live_server():
    server = StaticLiveServerTestCase()
    server.setUpClass()
    yield server
    server.tearDownClass()


@pytest.fixture(scope='session')
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture(scope='function')
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(5000)
    yield page
    context.close()
