from django.test import TestCase
from django.urls import reverse


class TestViews(TestCase):
    def test_upload_view(self):
        response = self.client.get(reverse('importcsv:upload'))
        assert response.status_code == 200
        self.assertTemplateUsed(response, 'importcsv/import_csv.html')
