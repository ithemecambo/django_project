from django.contrib.auth import get_user_model
from django.test import TestCase

from blogposts.models import *


class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='senghort', email='senghort@gmail.com', password='admin@@'
        )
        cls.post = BlogPost.objects.create(
            title='Welcome to our blog',
            author=cls.user,
            body='Blog posts should be concise and straight to the point.'
        )

    def test_blog_model(self):
        self.assertEqual(self.post.title, 'Welcome to our blog')
        self.assertEqual(self.post.author.username, 'senghort')
        self.assertEqual(self.post.body, 'Blog posts should be concise and straight to the point.')
        self.assertEqual(self.post.get_absolute_url(), '/blog-detail/1/')

    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get('/blog/blog-detail/1/')
        self.assertEqual(response.status_code, 200)

    def test_post_listview(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Blog posts should be concise and straight to the point.')
        self.assertTemplateUsed(response, 'blogs.html')

    def test_post_detailview(self):
        response = self.client.get(reverse('blog-detail', kwargs={'pk', self.post.pk}))
        no_response = self.client.get('/get/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Welcome to our blog')
        self.assertTemplateUsed(response, 'blog-detail.html')

    def test_post_createview(self):
        response = self.client.blogpost(reverse('blog-create'),
                                        {
                                            'title': 'New blog title',
                                            'body': 'New blog body',
                                            'author': self.user.id
                                        }
                                        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(BlogTest.objects.last().title, 'New blog title')
        self.assertEqual(BlogPost.objects.last().body, 'New blog body')

    def test_post_updateview(self):
        response = self.client.blogpost(reverse('blog-update', args="1"),
                                        {
                                            'title': 'New blog title was updated',
                                            'body': 'New blog body was updated',
                                        }
                                        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(BlogPost.objects.last().title, 'New blog title was updated')
        self.assertEqual(BlogPost.objects.last().body, 'New blog body was updated')

    def test_post_deleteview(self):
        response = self.client.blogpost(reverse('blog-delete', args="1"),)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.status_code, 302)
