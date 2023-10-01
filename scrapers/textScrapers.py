"""
Omodayo Origunwa
10.01.2023
"""

import nltk
import html2text
from lxml import etree
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod

class Parser(ABC):
    response = ''
    decoded_response = ''

    @abstractmethod
    def get_all_page_text(self):
        pass

    @abstractmethod
    def get_page_results(self):
        pass

class NLTKParser(Parser):

    def __init__(self, response):
        super().__init__()
        self.response = response
        self.decoded_response = response.text

    def get_all_page_text(self):
        html_text = self.decoded_response
        raw_text = nltk.clean_html(html_text)
        return raw_text

    def get_page_results(self):
        pass

class HTML2TextParser(Parser):

    def __init__(self, response):
        super().__init__()
        self.response = response
        self.decoded_response = response.text

    def get_all_page_text(self):
        html_text = self.decoded_response
        raw_html = html2text.html2text(html_text)
        return raw_html

    def get_page_results(self):
        pass
    
class Bs4Parser(Parser):

    def __init__(self, response):
        super().__init__()
        self.response = response
        self.decoded_response = response.text

    def get_all_page_text(self):
        html_text = self.decoded_response
        soup = BeautifulSoup(html_text)
        raw_text = soup.article.get_text(' ', strip=True)
        return raw_text

    def get_page_results(self, curClass='VwiC3b'):
        soup = BeautifulSoup(self.response.content, "html.parser")
        dom = etree.HTML(str(soup))
        page_results = dom.xpath(f"//div[contains(concat(' ',normalize-space(@class),' '),' {curClass} ')]")
        return page_results
