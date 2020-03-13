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
        transcription = self.parse.parse_transcription()
        self.assertEqual(transcription, '|ˈfaɪər|')

    def test_parse_definition(self):
        result = 'огонь'
        definition_ru = self.parse.parse_definition_ru()
        self.assertIn(result, definition_ru)
    
    def test_parse_phrases(self):
        result = 'to blanket the fire with sand'
        phrases = self.parse.parse_phrases()
        self.assertEqual(len(phrases), 10)
        self.assertIn(result, phrases[1]['eng'])

    def test_example(self):
        result = 'The house is on fire!'
        example = self.parse.parse_example()
        self.assertIn(result, example[1]['example_eng'])
        self.assertEqual(len(example), 30)
        
    def test_phrasal_verbs(self):
        result = 'fire away'
        verbs = self.parse.parse_phrasal_verbs()
        self.assertTrue(verbs)
        self.assertEqual(len(verbs), 4)
        self.assertIn(result, verbs[1]['phrasal_verbs'])
        

if __name__ == "__main__":
    unittest.main()

