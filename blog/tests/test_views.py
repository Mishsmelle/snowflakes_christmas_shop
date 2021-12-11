from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post, Comment


class TestViews(TestCase):
    ''' test views are correct'''
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testpassword'
        )
        self.blog_url = reverse('blog')
        self.blog_post_url = reverse('blog_post', args=['test1'])
        self.add_blog_post = reverse('add_blog_post')
        self.test1 = Post.objects.create(
            title='test1',
            user=self.user,
            intro="test1",
        )
        self.comment = Comment.objects.create(
            post=self.test1,
            user=self.user,
            body="Test Comment",
        )

    def test_blog_GET(self):
        response = self.client.get(self.blog_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')

    def test_blog_post_GET(self):
        response = self.client.get(self.blog_post_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_post.html')

    def test_add_blog_post_POST(self):
        response = self.client.post(self.blog_post_url, {
            'title': 'test1',
            'user': self.user,
            'intro': "test1",
        })

        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.test1.title, 'test1')

    def test_add_blog_post_POST_no_data(self):
        response = self.client.post(self.add_blog_post)

        self.assertEquals(response.status_code, 302)
