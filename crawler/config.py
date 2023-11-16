# Configuration equivalent to config.ts
class Config:
    def __init__(self, url, match, selector, max_pages_to_crawl, output_file_name, cookie=None, on_visit_page=None):
        self.url = url
        self.match = match
        self.selector = selector
        self.max_pages_to_crawl = max_pages_to_crawl
        self.output_file_name = output_file_name
        self.cookie = cookie
        self.on_visit_page = on_visit_page


