import unittest

from model import function, myunit
from Page_Object.LoginPage import *
from Page_Object.StaffPage import *
from Page_Object.DepartmentPage import *
from time import sleep


class LoginTest(myunit.StartEnd):

    def test_1(self):
        op = LoginPage(self.driver)
        op.login_interface()
        sleep(2)
        function.insert_img(self.driver, "d.png")

    # @unittest.skip("dd")
    def test_2(self):
        self.test_1()
        op = StaffPage(self.driver)
        op.yd_staff()
        sleep(2)
        function.insert_img(self.driver, "b.png")

    def test_3(self):
        self.test_1()
        op = DepartmentPage(self.driver)
        op.ya_department()
        function.insert_img(self.driver, 'c.png')


if __name__ == '__main__':
    unittest.main()
