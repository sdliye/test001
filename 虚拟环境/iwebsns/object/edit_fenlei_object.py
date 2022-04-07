# encoding: utf-8
'''
@author: xxx
@file: edit_fenlei_object.py
@time: 2022-04-01 11:09
@desc:
'''
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class EditFenlei:
    def __init__(self, driver):
        self.driver = driver
        self.ck_log_elem = By.LINK_TEXT, '日志'
        self.frame1_elem = 'frame_content'
        self.ck_cr_log_elem = By.LINK_TEXT, '新建日志'
        self.ck_log_fenlei_elem = By.LINK_TEXT, '日志分类'
        self.ck_edit_elem = By.XPATH, '//table/tbody/tr[2]/td[2]/div/a'
        self.ck_edit1_elem=By.XPATH,'/html[1]/body[1]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/a[2]'
        self.inp_name_elem = By.XPATH, '//table/tbody/tr[3]/td/input'
        self.ck_save_elem = By.XPATH, '//table/tbody/tr[3]/td[2]/input'
        self.text_elem = By.XPATH, '/html[1]/body[1]/table[1]/tbody[1]/tr[2]/td[1]/div[1]'

    def into_logfenlei(self):
        self.driver.find_element(*self.ck_log_elem).click()
        time.sleep(1)
        self.driver.switch_to.frame(self.frame1_elem)
        self.driver.find_element(*self.ck_cr_log_elem).click()
        time.sleep(1)
        self.driver.find_element(*self.ck_log_fenlei_elem).click()

    def ckedit(self):
        self.driver.find_element(*self.ck_edit_elem).click()
        time.sleep(1)
        self.driver.find_element(*self.inp_name_elem).clear()

    def ckdel(self):
        self.driver.find_element(*self.ck_edit1_elem).click()
        time.sleep(1)
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        time.sleep(1)

    def editlog(self, key1):
        self.driver.find_element(*self.inp_name_elem).clear()
        self.driver.find_element(*self.inp_name_elem).send_keys(key1)

    def editlog1(self):
        self.driver.find_element(*self.inp_name_elem).clear()
        self.driver.find_element(*self.inp_name_elem).send_keys(Keys.SPACE)

    def save(self):
        self.driver.find_element(*self.ck_save_elem).click()

    def get_text(self):
        return self.driver.find_element(*self.text_elem).text

    def get_text1(self):
        return self.driver.find_element(*self.ck_log_fenlei_elem).text
