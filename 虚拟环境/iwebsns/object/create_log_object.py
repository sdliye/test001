# encoding: utf-8
'''
@author: xxx
@file: create_log_object.py
@time: 2022-04-01 9:31
@desc:
'''
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CreateLog:
    def __init__(self, driver):
        self.driver = driver
        self.ck_log_elem = By.LINK_TEXT, '日志'
        self.frame1_elem = 'frame_content'
        self.frame2_elem = 'KINDEDITORIFRAME'
        self.ck_cr_log_elem = By.LINK_TEXT, '新建日志'
        self.inp_name01_elem = By.NAME, 'blog_title'
        self.inp_name02_elem = By.NAME, 'tag'
        self.inp_name03_elem = By.ID, 'KINDEDITORBODY'
        self.choice_classify_elem=By.NAME,'blog_sort_list'
        self.ck_queren_elem = By.XPATH, '//tr[8]//td[1]//input[1]'
        self.ck_queren1_elem=By.ID,'_ButtonCancel_0'
        self.ck_queren3_elem = By.XPATH,'/html[1]/body[1]/div[5]/div[2]/div[1]/input[1]'
        self.ck_cancel1_elem = By.XPATH,''
        self.ck_cancel1_elem = By.XPATH,'/html[1]/body[1]/div[5]/div[2]/div[1]/input[2]'
        self.get_text_elem = By.XPATH, '/html[1]/body[1]/dl[1]/dt[1]/strong[1]/a[1]'
        self.get_text1_elem = By.ID,'Message_undefined'

    def create_log(self):
        self.driver.find_element(*self.ck_log_elem).click()
        time.sleep(1)
        self.driver.switch_to.frame(self.frame1_elem)
        self.driver.find_element(*self.ck_cr_log_elem).click()
        time.sleep(1)

    def send_key1(self, key):
        self.driver.find_element(*self.inp_name01_elem).send_keys(key)

    def send_key2(self, key):
        self.driver.find_element(*self.inp_name02_elem).send_keys(key)

    def send_key3(self, key):
        self.driver.switch_to.frame(self.frame2_elem)
        self.driver.find_element(*self.inp_name03_elem).send_keys(key)

    def choiceclassify(self,key):
        select=self.driver.find_element(*self.choice_classify_elem)
        Select(select).select_by_visible_text(key)
        time.sleep(1)



    def setscrall(self):
        self.driver.switch_to.default_content()
        time.sleep(1)
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        time.sleep(1)

    def ck_quren(self):
        self.driver.switch_to.frame(self.frame1_elem)
        self.driver.find_element(*self.ck_queren_elem).click()

    def ck_quren02(self):
        self.driver.find_element(*self.ck_queren1_elem).click()

    def switchdefault(self):
        self.driver.switch_to.default_content()

    def switchiframe(self):
        self.driver.switch_to.frame(self.frame1_elem)


    def gettext(self):
        return self.driver.find_element(*self.get_text_elem).text

    def gettext02(self):
        return self.driver.find_element(*self.get_text1_elem).text
