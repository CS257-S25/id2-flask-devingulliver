import unittest
import sys
from io import StringIO

from app import *

class TestHomepage(unittest.TestCase):
    def test_route(self):
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects=True)
        self.assertIn(b"""Go to /details/&lt;isbn&gt; for information on a book.
    Here's a valid ISBN to get you started: 1423134540""", response.data)

class TestDetails(unittest.TestCase):
    def test_route(self):
        self.app = app.test_client()
        response = self.app.get('/details/1423134540', follow_redirects=True)
        self.assertIn(b"Details for Keys to the Repository by Melissa de la Cruz (2010, ISBN: 1423134540)", response.data)
    
    def test_invalid(self):
        self.app = app.test_client()
        response = self.app.get('/details/00010', follow_redirects=True)
        self.assertIn(b"No book with that ISBN found!", response.data)

class Test404(unittest.TestCase):
    def test_route(self):
        self.app = app.test_client()
        response = self.app.get('/dsjfhk', follow_redirects=True)
        self.assertIn(b"That page doesn't exist. Try going home.", response.data)