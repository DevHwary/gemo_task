from django.test import TestCase, RequestFactory
import unittest
from datetime import datetime, timedelta
import requests
from . views import list_top_100_language
from django.test import Client


class SimpleTest(unittest.TestCase):

    def test_url_status(self):
        """
        test github's url response that returns the top 100 trending repository 
        """
        today = datetime.now()
        thirty_days_ago = (today - timedelta(days=30)).strftime("%Y-%m-%d")
        url = "https://api.github.com/search/repositories?q=created:>{0}&sort=stars&order=desc&page=1&per_page=100".format(thirty_days_ago)
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)


    def test_list_top_100_language_view(self):
        """
        test the list_top_100_language view
        """
        c = Client()
        response = c.get('/trending_languages/top_100', HTTP_ACCEPT='application/json')
        self.assertEqual(response.status_code, 200)
