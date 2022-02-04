import re
from requests_html import HTML, HTMLSession
from statistics import mode
from itertools import dropwhile

from constants import ALLOWED_TAGS

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.raw = None
    
    def fetch(self):
        """
            Returns a dictionary of:
                1. All unique tags used in the document.
                2. Most commonly used tag.
                3. Longest path starting from root node to the descendent.
                4. Longest path starting from root node where the most popular tag is used the most times
        """
        unique_tags = []
        most_common_tag = ""
        paths = {}
        
        try:
            session = HTMLSession()
            req = session.get(self.url)
            self.raw = req.html.raw_html.decode("utf-8")
            all_tags = re.findall(r'<[^>]+>', self.raw)
            tags = self.modified_tags(all_tags)
            unique_tags = list(set(tags))
            most_common_tag = mode(tags)
            paths = self.longest_path(all_tags, most_common_tag)
            
        except Exception as e:
            print(e)
            
        return {
            "unique_tags": ', '.join(unique_tags),
            "most_common_tag": most_common_tag,
            "paths": paths
        }

    def longest_path(self, all_tags, most_common_tag):
        """
            Returns a dictionary of:
                1. longest_path: Longest path starting from root node to the descendent.
                2. times_used_list: Longest path starting from root node where the most popular tag is used the most times
        """
        try:
            # Remove all unnecessary tags, including <body>
            body_tags = list(dropwhile(lambda x: not x.startswith('<body'), all_tags))
            body_tags = [x for x in body_tags[0:body_tags.index('</body>')]]
            body_tags = body_tags[1:]
            sequence = []
            path = []
            
            # Recursively loop through the list and create multidimensional list of nestings
            for tag in body_tags[::-1]:
                stripped_tag = tag.split(' ')[0] + '>' if not tag.split(' ')[0].endswith('>') else tag.split(' ')[0]
                if stripped_tag.startswith('</'):
                    final_tag = stripped_tag.replace('<', '').replace('/', '').replace('>', '')
                    path.append(final_tag)
                else:
                    sequence.append(path)
                    path = []

            longest_path = max(sequence, key=len)
            times_tag_used = 0
            times_tag_used_list = []
            
            for seq in sequence:
                used = seq.count(most_common_tag.replace('<', '').replace('/', '').replace('>', ''))
                if used > times_tag_used:
                    times_tag_used = used
                    times_tag_used_list = seq
            
            return {
                "longest_path": ' > '.join(longest_path),
                "times_used_list": ' > '.join(times_tag_used_list)
            }
        except Exception as e:
            print(e)
            return {
                "longest_path": [],
                "times_used_list": []
            }
            
    def modified_tags(self, all_tags):
        """
            Returns all HTML tag openings used to identify unique tags and find most common tag
        """
        tags = []
        
        try:
            # Create tags list with only tag names (removes all atributes)
            for tag in all_tags:
                if not tag.startswith('</'):
                    stripped_tag = tag.split(' ')[0] + '>' if not tag.split(' ')[0].endswith('>') else tag.split(' ')[0]
                    tag_text = stripped_tag.replace('<', '').replace('>', '')
                    if tag_text in ALLOWED_TAGS:
                        tags.append(stripped_tag)
        except Exception as e:
            print(e)
        
        return tags
    
    
        
