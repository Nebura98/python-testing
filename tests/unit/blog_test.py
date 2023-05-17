from unittest import TestCase

from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        blog = Blog('Test', 'Test Author')

        self.assertEqual('Test', blog.title)
        self.assertEqual('Test Author', blog.author)
        self.assertListEqual([], blog.posts)
        self.assertEqual(0, len(blog.posts))

    def test_repr(self):
        blog = Blog('Test', 'Test Author')
        blog2 = Blog('My day', 'Pepe')

        self.assertEqual(blog.__repr__(), 'Test by Test Author (0 posts)')
        self.assertEqual(blog2.__repr__(), 'My day by Pepe (0 posts)')

    def test_repr_multiple_posts(self):
        blog = Blog('Test', 'Test Author')
        blog.posts = ['Test']

        blog2 = Blog('My day', 'Pepe')
        blog2.posts = ['Test', 'Another']

        self.assertEqual(blog.__repr__(), 'Test by Test Author (1 post)')
        self.assertEqual(blog2.__repr__(), 'My day by Pepe (2 posts)')