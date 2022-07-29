from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Snack

# Create your tests here.
class SnackTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test', email='test@@test.com',
            password='test@12345'
        )
        self.snack = Snack.objects.create(
            title="Test",
            purchaser=self.user,
        )

    def test_list_status(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_template(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')

    def test_detail_status(self):
        url = reverse("snack_detail", args=[self.snack.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_view(self):
        url = reverse('snack_detail', args=[self.snack.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snack_detail.html')

    def test_create_status(self):
        url = reverse("snack_create")
        data = {
            "title": "Test Create",
            "purchaser": self.user.id
        }
        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_create_view(self):
        url = reverse('snack_create')
        data = {
            "title": "Test Create",
            "purchaser": self.user.id
        }
        response = self.client.post(path=url, data=data, follow=True)
        self.assertTemplateUsed(response, 'snack_detail.html')

    def test_update_status(self):
        url = reverse("snack_update", args=[self.snack.id])
        data = {
            "title": "Test Create",
            "purchaser": self.user.id
        }
        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_update_view(self):
        url = reverse('snack_update', args=[self.snack.id])
        data = {
            "title": "Test Create",
            "purchaser": self.user.id
        }
        response = self.client.post(path=url, data=data, follow=True)
        self.assertTemplateUsed(response, 'snack_detail.html')

    def test_delete_status(self):
        url = reverse("snack_delete", args=[self.snack.id])
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_view(self):
        url = reverse('snack_delete', args=[self.snack.id])
        response = self.client.post(path=url, follow=True)
        self.assertTemplateUsed(response, 'snack_list.html')

    def test_str_method(self):
        self.assertEqual(str(self.snack), 'Test')