from unittest import TestCase

from blog import Blog


class BlogTest(TestCase):
    def test_create_post_on_blog(self):
        blog = Blog('Test', 'Test author')
        blog.create_post('Test post', 'Test content')

        self.assertEqual(len(blog.posts), 1)
        self.assertEqual(blog.posts[0].title, 'Test post')
        self.assertEqual(blog.posts[0].content, 'Test content')

    def test_json_no_posts(self):
        blog = Blog('Test', 'Test author')
        expected = {
            'title': 'Test',
            'author': 'Test author',
            'posts': []
        }

        self.assertDictEqual(expected, blog.json())

    def test_json(self):
        blog = Blog('Test', 'Test author')
        blog.create_post('Test post', 'Test content')

        expected = {
            'title': 'Test',
            'author': 'Test author',
            'posts': [{'title': 'Test post', 'content': 'Test content'}]
        }

        self.assertDictEqual(expected, blog.json())
