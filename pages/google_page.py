class GooglePage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://google.com")

    def get_title(self):
        return self.page.title()