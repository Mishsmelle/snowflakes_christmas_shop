from django.test import TestCase
from blog.models import Post, Comment
from django.contrib.auth.models import User


class TestModels(TestCase):
    ''' test models are correct'''
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testpassword'
        )
        self.post1 = Post.objects.create(
            title='Post 1',
            user=self.user,
        )

    def test_post_assigned_slug_on_creation(self):
        self.assertEquals(self.post1.slug, 'post-1')

    def test_post_model(self):
        post = Post.objects.create(
            title="Test Post",
            user=self.user,
            intro="Test Intro",
            body="Test Body",
        )
        self.assertEqual(str(post), "Test Post")

    def test_comment_model(self):
        self.client.login(
            username="testuser", password="testpassword")
        post = Post.objects.create(
            title="Test Post",
            user=self.user,
            intro="Test Intro",
            body="Test Body",
        )
        comment = Comment.objects.create(
            post=post,
            user=self.user,
            body="Test Comment",
        )
        self.assertEqual(str(comment), "Comment on Test Post by testuser")
