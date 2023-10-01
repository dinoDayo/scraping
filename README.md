# scraping
tools n tricks for web scraping

#### Project setup
- Modelled after docs linked [here](https://docs.python-guide.org/writing/structure/).

#### XPath selectors
- These are very helpful for debugging a given scraping script. [A cheat sheet I like is linked here](https://devhints.io/xpath).
    - GET text content related to each result in the Google SERP: `$x("//div[contains(concat(' ',normalize-space(@class),' '),' VwiC3b ')]")`
