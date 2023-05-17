from unittest import TestCase

from post import Post


class PostTest(TestCase):
    # Should start with the word test
    def test_create_post(self):
        post = Post('Test', 'Test content')
        self.assertEqual('Test', post.title)
        self.assertEqual('Test content', post.content)

    def test_json(self):
        post = Post('Test', 'Test content')
        expected = {'title': 'Test', 'content': 'Test content'}

        self.assertDictEqual(expected, post.json())
