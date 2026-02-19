from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase
from django.contrib.auth.models import User
from .models import Photo
'''
Testing Cases, this only test for API if the user is authenticated and the end points work as intended.
Further testing needed: test unauthorized users, test bad requests and if object does not exists

'''
class PhotoTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.photo = Photo.objects.create(
            width=500,
            height=500,
            url="test_url",
            photographer="test_photographer",
            photographer_url="test_photographer_url",
            photographer_id=9999,
            avg_color="test_avg_color",
            original="test_original",
            large2x="test_large2x",
            large="test_large",
            medium="test_medium",
            small="test_small",
            portrait="test_portrait",
            landscape="test_landscape",
            tiny="test_tiny",
            alt="test_alt"
        )
        self.test_id = self.photo.pk

    def test_unauthorized_get_photos(self):
        url = reverse('photo-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_photos(self):
        self.client.login(username='test_user', password='test_password')
        url = reverse('photo-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthorized_create_photos(self):
        url = reverse('photo-list')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_photos(self):
        self.client.login(username='test_user', password='test_password')
        url = reverse('photo-list')
        data = {
            "width": 500,
            "height": 500,
            "url": "test_url",
            "photographer": "test_photographer",
            "photographer_url": "test_photographer_url",
            "photographer_id": 9999,
            "avg_color": "test_avg_color",
            "original": "test_original",
            "large2x": "test_large2x",
            "large": "test_large",
            "medium": "test_medium",
            "small": "test_small",
            "portrait": "test_portrait",
            "landscape": "test_landscape",
            "tiny": "test_tiny",
            "alt": "test_alt"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unauthorized_get_photo_details(self):
        url = reverse('photo-details', kwargs={'photo_id': self.test_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_photo_details(self):
        self.client.login(username='test_user', password='test_password')
        url = reverse('photo-details', kwargs={'photo_id': self.test_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_dne_get_photo_details(self):
        self.client.login(username='test_user', password='test_password')
        url = reverse('photo-details', kwargs={'photo_id': 234234})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_unauthorized_update_photo_details(self):
        url = reverse('photo-details', kwargs={'photo_id': self.test_id})
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_photo(self):
        self.client.login(username='test_user', password='test_password')
        url = reverse('photo-details', kwargs={'photo_id': self.test_id})
        data = {
            "width": 500,
            "height": 500,
            "url": "test_url",
            "photographer": "test_photographer",
            "photographer_url": "test_photographer_url",
            "photographer_id": 9999,
            "avg_color": "test_avg_color_updated",
            "original": "test_original",
            "large2x": "test_large2x",
            "large": "test_large",
            "medium": "test_medium",
            "small": "test_small",
            "portrait": "test_portrait",
            "landscape": "test_landscape",
            "tiny": "test_tiny",
            "alt": "test_alt"
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('avg_color'), "test_avg_color_updated")

    def test_dne_update_photo_details(self):
        self.client.login(username='test_user', password='test_password')
        url = reverse('photo-details', kwargs={'photo_id': 234234})
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_bad_request_update_photo(self):
        self.client.login(username='test_user', password='test_password')
        url = reverse('photo-details', kwargs={'photo_id': self.test_id})
        data = {
            "photographer": "test_photographer",
            "photographer_url": "test_photographer_url",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unauthorized_delete_photo_details(self):
        url = reverse('photo-details', kwargs={'photo_id': self.test_id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_dne_delete_photo_details(self):
        self.client.login(username='test_user', password='test_password')
        url = reverse('photo-details', kwargs={'photo_id': 234234})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_photo(self):
        self.client.login(username='test_user', password='test_password')
        url = reverse('photo-details', kwargs={'photo_id': self.test_id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Photo.objects.filter(pk=self.photo.id).exists(), False)
