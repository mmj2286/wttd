__author__ = 'mmj2286'

# coding: utf-8
from django.test import TestCase
class HomepageTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_get(self):
        'GET / must return status code 200.'
        self.assertEqual(200, self.resp.status_code)

    def teste_template(self):
        self.assertTemplateUsed(self.resp, 'index.html')