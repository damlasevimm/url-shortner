from rest_framework import status
from rest_framework.test import APITestCase

import hashlib

class URLShorteningTestCase(APITestCase):
    def test_new_url(self):
        data = {'url': 'https://www.google.com'}
        response = self.client.post('/shorten/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_existing_url(self):
        data = {'url': 'https://www.google.com'}
        first_response = self.client.post('/shorten/', data)
        data = {'url': 'https://www.google.com'}
        second_response = self.client.post('/shorten/', data)
        self.assertEqual(second_response.status_code, status.HTTP_303_SEE_OTHER)

    def test_location_valid(self):
        data = {'url': 'https://www.google.com'}
        response = self.client.post('/shorten/', data)
        shortcode = hashlib.shake_256(data['url'].encode()).hexdigest(5)
        location = '/urls/' + shortcode
        self.assertEqual(response.data['location'], location)
