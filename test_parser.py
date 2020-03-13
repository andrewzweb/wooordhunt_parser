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
        self.assertFalse(get_page())

    def NOtest_get_page_get_target_page(self):
        resp = get_page(TargetUrl)
        self.assertEqual(resp.status_code, 200)

class ParsePageTest(unittest.TestCase):
    
    targetUrl = 'https://wooordhunt.ru/word/fire'
    response = get_page(targetUrl)
    parse = Parse(response)

    def test_parse_exist(self):
        self.assertTrue(Parse(self.response)) 

    def test_parse_title(self):
        self.assertEqual(self.parse.parse_title(), 'Fire')
    
    def test_parse_transcription(self):
        self.assertEqual(self.parse.parse_transcription(), '|ˈfaɪər|')

    def test_parse_definition(self):
        result = 'огонь'
        self.assertIn(result, self.parse.parse_definition_ru())

    
    def test_parse_phrases(self):
        result = 'to blanket the fire with sand'
        self.assertEqual(len(self.parse.parse_phrases()), 10)
        self.assertIn(result, self.parse.parse_phrases()[1]['eng'])
        

if __name__ == "__main__":
    unittest.main()

