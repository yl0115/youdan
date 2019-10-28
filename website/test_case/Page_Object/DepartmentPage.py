from BasePage import *
from selenium.webdriver.common.by import By
import time


class DepartmentPage(Page):
    # 点击部门管理
    department = (By.XPATH, r'//*[@id="app"]/div/div[2]/ul/li[2]')
    # 点击新建按钮
    add = (By.XPATH, r'//*[@id="app"]/div/div[3]/div[2]/section/main/div[1]/button[1]')

    def ya_department(self):
        self.driver.find_element(*self.department).click()
        self.driver.find_element(*self.add).click()

