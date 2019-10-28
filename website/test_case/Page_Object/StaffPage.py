from BasePage import *
from selenium.webdriver.common.by import By
import time


class StaffPage(Page):
    # 员工管理点击链接
    staff = (By.XPATH, r'//*[@id="app"]/div/div[2]/ul/li[1]')
    # 点击新增员工按钮
    addButton = (By.XPATH, r'//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[1]/button[1]')
    # 新增界面输入姓名
    addName = (By.XPATH, r'//*[@id="app"]/div/div[3]/div[2]/div/div[5]/div/div[2]/div[1]/div'
                         r'[1]/form/div[1]/div/div[1]/input')
    # 新增界面登录名
    addLoginUser = (By.XPATH, r'//*[@id="app"]/div/div[3]/div[2]/div/div[5]/div/div[2]/div[1]/div'
                              r'[2]/form/div[1]/div/div/input')
    # 新增界面登录密码
    addLoginPassWorld = (By.XPATH, r'//*[@id="app"]/div/div[3]/div[2]/div/div[5]/div/div[2]/div[1]/div'
                                   r'[1]/form/div[2]/div/div/input')
    # 新增界面年龄
    addGge = (By.XPATH, r'//*[@id="app"]/div/div[3]/div[2]/div/div[5]/div/div[2]/div[1]/div'
                        r'[2]/form/div[2]/div/div/div/input')
    # 新增界面职务
    addDuty = (By.XPATH, r'//*[@id="app"]/div/div[3]/div[2]/div/div[5]/div/div[2]/div[1]/div'
                         r'[1]/form/div[3]/div/div/input')
    # 新增界面邮箱
    addEmail = (By.XPATH, r'//*[@id="app"]/div/div[3]/div[2]/div/div[5]/div/div[2]/div[1]/div'
                          r'[2]/form/div[3]/div/div/input')
    # 新增界面电话
    addTel = (By.XPATH, r'//*[@id="app"]/div/div[3]/div[2]/div/div[5]/div/div[2]/div[1]/div'
                        r'[1]/form/div[4]/div/div/input')
    # 新增界面民族
    addNation = (By.XPATH, r'//*[@id="app"]/div/div[3]/div[2]/div/div[5]/div/div[2]/div'
                           r'[1]/div[2]/form/div[4]/div/div/input')
    # 新增界面住址
    addAddress = (By.XPATH, r'//*[@id="app"]/div/div[3]/div[2]/div/div[5]/div/div[2]/div'
                            r'[1]/div[1]/form/div[5]/div/div/input')
    # 新增界面婚否
    addHun = (By.XPATH, r'//*[@id="app"]/div/div[3]/div[2]/div/div[5]/div/div[2]/div[1]'
                        r'/div[2]/form/div[5]/div/div/label[1]/span[1]/span')
    # 新增界面是否激活
    addActivate = (By.XPATH, r'//*[@id="app"]/div/div[3]/div[2]/div/div[5]/div/div[2]/div'
                             r'[1]/div[1]/form/div[6]/div/div/label[1]/span[1]/span')
    # 新增界面入职时间
    addTime = (By.XPATH, r'//*[@id="app"]/div/div[3]/div[2]/div/div[5]/div/div[2]/div'
                         r'[1]/div[2]/form/div[6]/div/div/input')
    # 新增及没按性别
    addSex = (By.XPATH, r'//*[@id="app"]/div/div[3]/div[2]/div/div[5]/div/div[2]/div'
                        r'[1]/div[1]/form/div[7]/div/div/label[1]/span[1]/span')
    # 新增界面备注
    addRemark = (By.XPATH, r'//*[@id="app"]/div/div[3]/div[2]/div/div[5]/div/div[2]/div[1]/div'
                           r'[1]/form/div[8]/div/div/textarea')
    # 新增界面说明
    addExplain = (By.XPATH, r'//*[@id="app"]/div/div[3]/div[2]/div/div[5]/div/div[2]/div'
                            r'[1]/div[2]/form/div[8]/div/div/textarea')
    # 新增界面确定按钮
    addNotarize = (By.XPATH, r'//*[@id="app"]/div/div[3]/div[2]/div/div[5]/div/div[2]/div[2]/span/button[2]')
    # 新增界面点击确定按钮后的确定
    addNotarize1 = (By.XPATH, r'/html/body/div[3]/div/div[3]/button[2]')
    # 新增界面点击确定按钮后的取消
    addCancel = (By.XPATH, r'/html/body/div[2]/div/div[3]/button[1]')
    # 方框
    a = (By.T, r'el-button el-button--default el-button--small el-button--primary')

    def yd_staff(self):
        time.sleep(3)
        self.driver.find_element(*self.staff).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.addButton).click()
        self.driver.find_element(*self.addName).send_keys('优单')
        self.driver.find_element(*self.addLoginUser).send_keys('66666666666666')
        self.driver.find_element(*self.addLoginPassWorld).send_keys('123456')
        self.driver.find_element(*self.addGge).send_keys('18')
        self.driver.find_element(*self.addDuty).send_keys('教师')
        self.driver.find_element(*self.addEmail).send_keys('1429068@qq.com')
        self.driver.find_element(*self.addTel).send_keys('18385656542')
        self.driver.find_element(*self.addNation).send_keys('汉')
        self.driver.find_element(*self.addAddress).send_keys('成都市金牛区')
        self.driver.find_element(*self.addHun).click()
        self.driver.find_element(*self.addActivate).click()
        self.driver.find_element(*self.addTime).send_keys('2019-06-12')
        self.driver.find_element(*self.addSex).click()
        self.driver.find_element(*self.addRemark).send_keys('你好')
        self.driver.find_element(*self.addExplain).send_keys('大家好')
        self.driver.find_element(*self.addNotarize).click()
        self.driver.find_element(*self.a).click()
        self.driver.implicitly_wait(100)
        # self.driver.find_element(*self.addNotarize1).click()



        # time.sleep(3)
        # self.driver.find_element(*self.addNotarize).click()
        #
        # self.driver.find_element(*self.addNotarize1).click()
        # self.driver.find_element(*self.a).click()




