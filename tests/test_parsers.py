
from context import scrapers
from scrapers import textScrapers, webCrawlers

# build request url
result_count="50"
search_terms="Hello World"
url = webCrawlers.build_request_url(search_terms=search_terms, result_count=result_count)

# exec request
res = webCrawlers.get_webpage(url=url)

# parse the result
breakpoint()
bs4Parser = textScrapers.Bs4Parser(response=res)
page_resuls = bs4Parser.get_page_results()
for result in page_resuls:
    print("\n", result.text, "\n")