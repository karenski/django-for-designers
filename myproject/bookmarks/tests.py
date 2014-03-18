"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.contrib.auth.models import User
from bookmarks.models import Bookmark


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 3)

class BookmarkViewTest(TestCase):
	def test_bookmark_show_up(self):
		me = User.objects.create(username='me')
		mark = Bookmark.objects.create(author=me, title='Title of the song', url='http://example.com/')
		c=Client()
		response = c.get('/')
		as_sent_to_template = response.context['bookmarks']
		self.assertTrue(mark in as_sent_to_template)
