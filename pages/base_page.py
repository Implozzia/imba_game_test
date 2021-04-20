class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.maximize_window()

    def open(self):
        self.browser.get(self.url)
