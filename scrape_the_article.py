# scraped_the_article.py 
"""is a Python script that scrapes the title and content of a webpage using BeautifulSoup and requests."""

import requests
from bs4 import BeautifulSoup

class ArticleScraper:
    def __init__(self, url):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        self.soup = None

    def fetch_content(self):
        """Fetches the webpage content and stores it in a BeautifulSoup object."""
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            self.soup = BeautifulSoup(response.content, 'html.parser')
        else:
            raise Exception(f"Failed to retrieve content. Status code: {response.status_code}")

    def extract_title(self):
        """Extracts and returns the title of the webpage."""
        if self.soup and self.soup.title:
            return self.soup.title.string
        return None

    def extract_content(self):
        """Extracts and returns all <h1> to <h6> and <p> tags in order."""
        if self.soup:
            content = self.soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p'])
            return [element.get_text() for element in content]
        return []

    def get_full_text(self):
        """Returns the title and content combined."""
        title = self.extract_title()
        content = self.extract_content()
        return title, '\n'.join(content)
