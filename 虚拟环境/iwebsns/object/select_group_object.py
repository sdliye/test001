# encoding: utf-8
'''
@author: xxx
@file: select_group_object.py
@time: 2022-04-05 12:44
@desc:
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class SelectGroup:
    def __init__(self, driver):
        self.driver = driver
        self.ck_group_elem=By.LINK_TEXT,'群组'
        self.frame1_elem='frame_content'
        self.ck_group01_elem = By.LINK_TEXT, '搜索群组'
        self.inp_name1_elem=By.ID,'group_name'
        self.inp_name2_elem=By.ID,'tag'
        self.choice_elem=By.ID,'group_type'
        self.ck_select_elem=By.CLASS_NAME,'regular-btn'
        self.get_text_elem=By.XPATH,'/html[1]/body[1]/div[3]/div[1]/dl[1]/dt[1]'

    def intogroup(self):
        self.driver.find_element(*self.ck_group_elem).click()
        self.driver.switch_to.frame(self.frame1_elem)
        self.driver.find_element(*self.ck_group01_elem).click()

    def selectgroup(self,key1,key2,choice):
        self.driver.find_element(*self.inp_name1_elem).send_keys(key1)
        self.driver.find_element(*self.inp_name2_elem).send_keys(key2)
        select=self.driver.find_element(*self.choice_elem)
        Select(select).select_by_visible_text(choice)
        self.driver.find_element(*self.ck_select_elem).click()

    def gettext(self):
        return self.driver.find_element(*self.get_text_elem).text








