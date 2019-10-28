from selenium import webdriver
from Page_Object.BasePage import *


def browser():
    driver = webdriver.Chrome()
    driver.get(r'http://192.168.3.250:8080/dist/index.html')
    return driver


if __name__ == '__main__':
    browser()
