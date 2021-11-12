from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import (
                        blog, blog_post, add_blog_post,
                        edit_blog_post, delete_blog_post,
                        delete_comment)


class Test_urls(SimpleTestCase):
    ''' test urls are correct'''
    def test_blog_resolves(self):
        url = reverse('blog')
        print(resolve(url))
        self.assertEquals(resolve(url).func, blog)

    def test_blog_post_resolves(self):
        url = reverse('blog_post', args=['some-text'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, blog_post)

    def test_add_blog_post_resolves(self):
        url = reverse('add_blog_post')
        print(resolve(url))
        self.assertEquals(resolve(url).func, add_blog_post)

    def test_edit_blog_post_resolves(self):
        url = reverse('edit_blog_post', args=[2])
        print(resolve(url))
        self.assertEquals(resolve(url).func, edit_blog_post)

    def test_delete_blog_post_resolves(self):
        url = reverse('delete_blog_post', args=[2])
        print(resolve(url))
        self.assertEquals(resolve(url).func, delete_blog_post)

    def test_delete_comment_resolves(self):
        url = reverse('delete_comment', args=[2])
        print(resolve(url))
        self.assertEquals(resolve(url).func, delete_comment)