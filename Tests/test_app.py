"""Tests for the app.py Flask app."""
import unittest
from app import app

class TestEntireApp(unittest.TestCase):
    """Test all routes of the Flask app in this class."""
    def setUp(self):
        """Prepare the app for testing."""
        self.app = app.test_client()

    def test_homepage(self):
        """Test the index route (/)."""
        response = self.app.get('/', follow_redirects=True)
        self.assertIn(b"""Go to /details/&lt;isbn&gt; for information on a book.
    Here's a valid ISBN to get you started: 1423134540""", response.data)

    def test_details(self):
        """Test the details route (/details/ISBN)."""
        response = self.app.get('/details/1423134540', follow_redirects=True)
        self.assertIn(b"Details for Keys to the Repository by Melissa de la Cruz", response.data)

    def test_details_invalid(self):
        """If invalid input passed"""
        response = self.app.get('/details/00010', follow_redirects=True)
        self.assertIn(b"No book with that ISBN found!", response.data)

    def test_404(self):
        """Test the 404 route."""
        response = self.app.get('/dsjfhk', follow_redirects=True)
        self.assertIn(b"That page doesn't exist. Try going home.", response.data)
