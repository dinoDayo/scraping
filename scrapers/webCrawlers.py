import requests
from requests.utils import requote_uri

def build_request_url(search_terms, result_count):
    unecnoded_url = f"http://www.google.com/search?q={search_terms}&num={result_count}"
    return requote_uri(unecnoded_url)

def get_webpage(url):
    response = requests.get(url=url)
    return response 

# TODO: fill out requests with headers, ssl_verify flags, etc. B/c returned class names are inconsistent unless a proxy etc. are used.