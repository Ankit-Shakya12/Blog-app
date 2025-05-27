from django.test import TestCase , Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post

# Create your tests here.

class BlogTest(TestCase):

    def setUp(self):

        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@gmail.com',
            password='12345678',
        )

        self.post = Post.objects.create(
            title = 'test',
            body = 'Nice good ok',
            author = self.user,
        )

    def test_str_representation(self):
        post = Post(title = 'title test')
        self.assertEqual(str(post),post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}','test')
        self.assertEqual(f'{self.post.author}','testuser')
        self.assertEqual(f'{self.post.body}','Nice good ok')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'Nice good ok')
        self.assertTemplateUsed(response,'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/10000/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response,'test')
        self.assertTemplateUsed(response,'post_detail.html')
