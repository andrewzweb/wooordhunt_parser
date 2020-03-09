import unittest 
import pytest
from wooordhunt_parser import *


class BaseSettingsTest(unittest.TestCase):
    def test_base_url_exist(self):
        self.assertTrue(MainUrl)

    def test_target_url_exist(self):
        self.assertTrue(TargetUrl)

class GetPageTest(unittest.TestCase):

    def test_get_url_exist(self):
        self.assertTrue(get_page())

    def test_get_page_get_target_page(self):
        resp = get_page(TargetUrl)
        self.assertEqual(resp.status_code, 200)


if __name__ == "__main__":
    unittest.main()

