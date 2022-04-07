# encoding: utf-8
'''
@author: xxx
@file: upload_photo_object.py
@time: 2022-04-01 15:31
@desc:
'''
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class UploadPhoto:
    def __init__(self, driver):
        self.driver = driver
        self.ck_photo_elem = By.LINK_TEXT, '相册'
        self.fram01_elem = 'frame_content'
        self.ck_photo1_elem = By.LINK_TEXT, '上传相片'
        self.ck_sw_photo_elem = By.LINK_TEXT, '切换上传方式'
        self.ck_photo2_elem = By.ID, 'album_name'
        self.up_photo_elem = By.ID, 'attach[]'
        self.ck_cofirm_elem = By.CLASS_NAME, 'regular-btn'
        self.inp_name_elem = By.CLASS_NAME, 'small-text'
        self.inp_name1_elem = By.CLASS_NAME, 'med-textarea'
        self.ck_fengmian_elem = By.NAME, 'album_skin'
        self.ck_cofirm1_elem = By.NAME, 'action'
        self.gettext_elem = By.CLASS_NAME, 'album_edit'

    def into_photo(self):
        self.driver.find_element(*self.ck_photo_elem).click()
        time.sleep(1)
        self.driver.switch_to.frame(self.fram01_elem)
        self.driver.find_element(*self.ck_photo1_elem).click()

    def upload_pictures(self, text,path):
        self.driver.find_element(*self.ck_sw_photo_elem).click()
        time.sleep(1)
        select=self.driver.find_element(*self.ck_photo2_elem)
        Select(select).select_by_visible_text(text)
        time.sleep(1)
        self.driver.find_element(*self.up_photo_elem).send_keys(path)
        time.sleep(1)
        self.driver.find_element(*self.ck_cofirm_elem).click()

    def ck_cofirm(self, key1, key2):
        self.driver.find_element(*self.inp_name_elem).send_keys(key1)
        self.driver.find_element(*self.inp_name1_elem).send_keys(key2)
        self.driver.find_element(*self.ck_fengmian_elem).click()
        self.driver.find_element(*self.ck_cofirm1_elem).click()

    def gettext(self):
        return self.driver.find_element(*self.gettext_elem).text
