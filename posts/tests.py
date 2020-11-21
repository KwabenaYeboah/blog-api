from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post

class BlogTest(TestCase):
    @classmethod

    def setUpTestData(cls):
        #Creating a User
        testuser = User.objects.create_user(username='testuser',
                    password='abc123')
        testuser.save()

        #creating a blog post
        test_post = Post.objects.create(author=testuser, title='Blog Title',
                    content='Content Message')
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        content = f'{post.content}'
        self.assertEqual(author, 'testuser')
        self.assertEqual(title, 'Blog Title')
        self.assertEqual(content, 'Content Message')



