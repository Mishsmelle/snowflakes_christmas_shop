from django.test import SimpleTestCase
from blog.forms import PostForm, CommentForm


class TestForms(SimpleTestCase):
    ''' Test the forms in blog'''
    def test_Post_Form_valid_data(self):
        form = PostForm(data={
            'title': 'test title',
            'intro': 'test intro',
            'body': 'test'
        })

        self.assertTrue(form.is_valid())

    def test_post_form_invalid(self):
        form = PostForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    def test_Comment_Form_valid_data(self):
        form = CommentForm(data={
            'body': 'test',
        })

        self.assertTrue(form.is_valid())

    def test_Comment_form_invalid(self):
        form = CommentForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
