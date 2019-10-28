from BasePage import *
from selenium.webdriver.common.by import By


class LoginPage(Page):
    # 账号密码
    userName = "youdan"
    passWorld = 123456
    # 登录界面账号输入框
    loginInput = (By.XPATH, r'//*[@id="app"]/div/div/form/div[1]/div/div[1]/input')
    # 登录界面密码输入框
    loginPassWorld = (By.XPATH, r'//*[@id="app"]/div/div/form/div[2]/div/div[1]/input')
    # 登录界面登录按钮
    loginSubmit = (By.XPATH, r'//*[@id="app"]/div/div/form/div[3]/button')

    def login_interface(self):
        self.find_element(*self.loginInput).clear()
        self.find_element(*self.loginInput).send_keys(self.userName)
        self.find_element(*self.loginPassWorld).clear()
        self.find_element(*self.loginPassWorld).send_keys(self.passWorld)
        self.find_element(*self.loginSubmit).click()




