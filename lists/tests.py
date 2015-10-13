from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string

class HomePageTest(TestCase):
  def test_root_url_resolves_to_home_page(self):
    found = resolve('/')
    self.assertEqual(found.func, home_page)

  def test_home_page_returns_html(self):
    request = HttpRequest()
    response = home_page(request)
    expected_html = render_to_string("home.html")
    self.assertEqual(response.content.decode(), expected_html)
#    self.assertTrue(response.content.startswith(b'<html>'))
#    self.assertTrue(response.content.strip().endswith(b'</html>')) # Use of templates creating extra whitespace
#    self.assertIn(b'<title>To-Do Lists</title>', response.content)
