from django.test import TestCase
from django.urls import reverse


class HomePageTestCase(TestCase):
    def test_url_exists_correct_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'pages/home.html')

    def test_template_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, '<h1>Home Page</h1>')


class AboutPageTestCase(TestCase):
    def test_url_exists_correct_location(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_template_by_correct(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'pages/about.html')

    def test_template_content(self):
        response = self.client.get(reverse('about'))
        self.assertContains(response, '<h1>About Page</h1>')
