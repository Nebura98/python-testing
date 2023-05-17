from unittest import TestCase
from unittest.mock import patch

import main
from blog import Blog
from post import Post


class MainTest(TestCase):
    def setUp(self):
        blog = Blog('Test', 'Test author')
        main.blogs = {'Test': blog}

    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mocked_input:
            with patch('main.ask_create_blog') as mocked_ask_create_blog:
                mocked_input.side_effect = ('c', 'Test create blog', 'Test author', 'q')
                main.menu()

                mocked_ask_create_blog.assert_called()

    def test_menu_print_prompt(self):
        with patch('builtins.input', return_value='q') as mocked_input:
            main.menu()
            mocked_input.assert_called_with(main.MENU_PROMPT)

    def test_menu_calls_print_blogs(self):
        with patch('main.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                main.menu()
                mocked_print_blogs.assert_called_with()

    def test_print_blogs(self):
        with patch('builtins.print') as mocked_print:
            main.print_blogs()
            mocked_print.assert_called_with('- Test by Test author (0 posts)')

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test author')
            main.ask_create_blog()

            self.assertIsNotNone(main.blogs.get('Test'))

    def test_ask_read_blog(self):
        with patch('builtins.input', return_value='Test'):
            with patch('main.print_posts') as mocked_print_posts:
                main.ask_read_blog()
                mocked_print_posts.assert_called_with(main.blogs['Test'])

    def test_print_posts(self):
        blog = main.blogs['Test']

        blog.create_post('Test post', 'Test content')

        with patch('main.print_post') as mocked_print_post:
            main.print_posts(blog)

            mocked_print_post.assert_called_with(blog.posts[0])

    def test_print_post(self):
        post = Post('Post title', 'Post content')
        expected_print = '''
---Post title---

Post content
'''
        with patch('builtins.print') as mocked_print:
            main.print_post(post)
            mocked_print.assert_called_with(expected_print)

    def test_ask_create_post(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test title', 'Test content')

            main.ask_create_post()

            self.assertEqual(main.blogs['Test'].posts[0].title, 'Test title')
            self.assertEqual(main.blogs['Test'].posts[0].content, 'Test content')
