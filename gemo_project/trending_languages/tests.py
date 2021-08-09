from django.test import TestCase
import unittest
from datetime import datetime, timedelta
import requests


class SimpleTest(unittest.TestCase):

    def test_url_status(self):
        today = datetime.now()
        thirty_days_ago = (today - timedelta(days=30)).strftime("%Y-%m-%d")
        url = "https://api.github.com/search/repositories?q=created:>{0}&sort=stars&order=desc&page=1&per_page=100".format(thirty_days_ago)
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
