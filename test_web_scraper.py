import unittest

from scraper.webscraper import WebScraper
from tests_constants import FINAL_TAGS, PATHS_RESULT, RAW_TAGS

class TestWebScraper(unittest.TestCase):
    def test_modifies_tags_as_required(self):
        scraper = WebScraper(url='https://google.com')
        tags = scraper.modified_tags(RAW_TAGS)
        self.assertEqual(tags, FINAL_TAGS)
    
    def test_longest_path(self):
        scraper = WebScraper(url='https://google.com')
        paths = scraper.longest_path(all_tags=RAW_TAGS, most_common_tag='<div>')
        self.assertEqual(paths, PATHS_RESULT)
        