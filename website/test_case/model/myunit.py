from driver.dirver import *
import unittest
import time


class StartEnd(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.implicitly_wait(6)
        time.sleep(3)
        self.driver.quit()

