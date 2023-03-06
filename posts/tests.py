from django.test import TestCase
from django.urls import reverse

from .models import Post


class PostTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text='This is a post for Testing.')

    def test_model_content(self):
        self.assertEqual(self.post.text, 'This is a post for Testing.')

    def test_url_exist_correct_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse('posts'))
        self.assertTemplateUsed(response, 'posts.html')

    def test_template_content(self):
        response = self.client.get(reverse('posts'))
        self.assertContains(response, 'This is a post for Testing.')

    def test_post_all(self):
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts.html')
        self.assertContains(response, 'This is a post for Testing.')
