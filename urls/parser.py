from bs4 import BeautifulSoup
import requests


class Parser:
    def __init__(self, url):
        self.url = url

    def parse_page(self):
        response = requests.get(self.url)

        if response.status_code != 200:
            return False

        soup = BeautifulSoup(response.content, 'html.parser')

        tags_to_search = ["og:title", "og:description", "og:image", "og:type"]

        fallback_tags = None
        found_tags = {}

        for og_tag in tags_to_search:
            new_found_tag = soup.find("meta", property=og_tag)
            if new_found_tag is not None:
                found_tags[new_found_tag["property"]] = new_found_tag["content"]
            elif fallback_tags is not None and og_tag in fallback_tags:
                found_tags[og_tag] = soup.find(fallback_tags[og_tag]).text

        if not found_tags.get("og:title"):
            found_tags["og:title"] = soup.title.text
        if not found_tags.get("og:type"):
            found_tags["og:type"] = "website"

        return found_tags

