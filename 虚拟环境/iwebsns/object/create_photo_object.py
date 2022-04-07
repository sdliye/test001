# encoding: utf-8
'''
@author: xxx
@file: create_photo_object.py
@time: 2022-04-01 15:47
@desc:
'''
import time
from selenium.webdriver.common.by import By


class CreatePhoto:
    def __init__(self, driver):
        self.driver = driver
        self.ck_photo_elem = By.LINK_TEXT, '相册'
        self.ck_crphoto_elem = By.LINK_TEXT, '新建相册'
        self.frame1_elem = 'frame_content'
        self.inp_name1_elem = By.ID, 'album_name'
        self.inp_name2_elem = By.ID, 'album_information'
        self.inp_name3_elem = By.ID, 'tag'
        self.ck_cr_elem = By.NAME, 'action'
        self.ck_myphoto_elem = By.LINK_TEXT, '我的相册'
        self.ck_true_elem=By.ID,'_ButtonCancel_0'
        self.text_elem = By.XPATH, '/html[1]/body[1]/div[4]/dl[1]/dd[1]/strong/a'
        self.text1_elem=By.ID,'Message_undefined'

    def ckphoto(self):
        self.driver.find_element(*self.ck_photo_elem).click()
        self.driver.switch_to.frame(self.frame1_elem)
        self.driver.find_element(*self.ck_crphoto_elem).click()
        time.sleep(1)

    def sendname1(self, key):
        self.driver.find_element(*self.inp_name1_elem).send_keys(key)

    def sendname2(self, key):
        self.driver.find_element(*self.inp_name2_elem).send_keys(key)

    def sendname3(self, key):
        self.driver.find_element(*self.inp_name3_elem).send_keys(key)

    def cktrue(self):
        self.driver.find_element(*self.ck_cr_elem).click()
    def cktrue1(self):
        self.driver.find_element(*self.ck_true_elem).click()

    def ckmyphoto(self):
        self.driver.find_element(*self.ck_myphoto_elem).click()

    def swdefault(self):
        self.driver.switch_to.default_content()

    def gettext(self):
        return self.driver.find_element(*self.text_elem).text

    def gettext1(self):
        return self.driver.find_element(*self.text1_elem).text
