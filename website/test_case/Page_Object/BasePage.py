import logging


class Page():
    def __init__(self, driver):
        self.driver = driver
        self.baseUrl = ''
        self.timeout = 1

    def _open(self, url):
        self.url_ = self.baseUrl+url
        logging.info('this Page is %s' % self.url_)
        self.driver.maximize_window()
        self.driver.get(self.url_)
        self.driver.implicitly_wait(5)
        assert self.driver.current_url == self.url_, 'Did not land on %s' % self.url_

    def open(self, url):
        self._open(url)

    def find_element(self, *loc):
        """封装查找元素类"""
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        """封装查找多个元素类"""
        return self.driver.find_elements(*loc)

