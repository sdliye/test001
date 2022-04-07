# encoding: utf-8
'''
@author: xxx
@file: login_object.py
@time: 2022-03-31 14:56
@desc:
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.user_elem = By.ID, 'login_email'
        self.pass_elem = By.ID, 'login_pws'
        self.ck_login_elem = By.ID, 'loginsubm'
        self.exit_elem = By.LINK_TEXT, '退出'
        self.get_text_elem = By.LINK_TEXT, '我的主页'
        self.get_text1_elem = By.ID, 'pwdmsg'
        self.get_text2_elem = By.ID, 'emailmsg'

    def user_paswd(self, username, password):
        self.driver.find_element(*self.user_elem).clear()
        self.driver.find_element(*self.pass_elem).clear()
        self.driver.find_element(*self.user_elem).send_keys(username)
        self.driver.find_element(*self.pass_elem).send_keys(password)
        self.driver.find_element(*self.ck_login_elem).click()

    def user_paswd02(self, username):
        self.driver.find_element(*self.user_elem).clear()
        self.driver.find_element(*self.pass_elem).clear()
        self.driver.find_element(*self.user_elem).send_keys(username)
        self.driver.find_element(*self.ck_login_elem).click()

    def user_paswd03(self, username):
        self.driver.find_element(*self.user_elem).clear()
        self.driver.find_element(*self.pass_elem).clear()
        self.driver.find_element(*self.user_elem).send_keys(username)
        self.driver.find_element(*self.pass_elem).send_keys(Keys.SPACE)
        self.driver.find_element(*self.ck_login_elem).click()

    def user_paswd04(self,password):
        self.driver.find_element(*self.user_elem).clear()
        self.driver.find_element(*self.pass_elem).clear()
        self.driver.find_element(*self.pass_elem).send_keys(password)
        self.driver.find_element(*self.ck_login_elem).click()

    def user_paswd05(self,password):
        self.driver.find_element(*self.user_elem).clear()
        self.driver.find_element(*self.pass_elem).clear()
        self.driver.find_element(*self.user_elem).send_keys(Keys.SPACE)
        self.driver.find_element(*self.pass_elem).send_keys(password)
        self.driver.find_element(*self.ck_login_elem).click()

    def exit(self):
        self.driver.switch_to.default_content()
        js = "var q=document.documentElement.scrollTop=1"
        self.driver.execute_script(js)
        self.driver.find_element(*self.exit_elem).click()


    def gettest(self):
        return self.driver.find_element(*self.get_text_elem).text

    def gettest01(self):
        return self.driver.find_element(*self.get_text1_elem).text

    def gettest02(self):
        return self.driver.find_element(*self.get_text2_elem).text