# encoding: utf-8
'''
@author: xxx
@file: create_group_object.py
@time: 2022-04-02 15:37
@desc:
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class CreateGroup:
    def __init__(self, driver):
        self.driver = driver
        self.ck_group_elem=By.LINK_TEXT,'群组'
        self.frame1_elem='frame_content'
        self.ck_group01_elem=By.LINK_TEXT,'创建群组'
        self.ck1_elem=By.NAME,'action'
        self.ck_queren1_elem = By.ID, '_ButtonCancel_0'
        self.inp_name01_elem=By.ID,'group_name'
        self.inp_name02_elem=By.ID,'group_resume'
        self.inp_name03_elem = By.ID, 'tag'
        self.choise1_elem=By.NAME,'group_join_type'
        self.choise2_elem=By.ID,'group_type'
        self.choise3_elem = By.ID, 'group_logo'
        self.get_text_elem=By.XPATH,'/html[1]/body[1]/div[4]/div[1]/dl[1]/dt[1]/a[1]'
        self.get_tex1_elem = By.ID,'Message_undefined'


    def creategoup(self):
        self.driver.find_element(*self.ck_group_elem).click()
        self.driver.switch_to.frame(self.frame1_elem)
        self.driver.find_element(*self.ck_group01_elem).click()

    def inpkey(self,key1,key2,choise1,key3,choise2,file):
        self.driver.find_element(*self.inp_name01_elem).send_keys(key1)
        self.driver.find_element(*self.inp_name02_elem).send_keys(key2)
        select=self.driver.find_element(*self.choise1_elem)
        Select(select).select_by_visible_text(choise1)
        self.driver.find_element(*self.inp_name03_elem).send_keys(key3)
        select = self.driver.find_element(*self.choise2_elem)
        Select(select).select_by_visible_text(choise2)
        self.driver.find_element(*self.choise3_elem).send_keys(file)

    def ckcreate(self):
        self.driver.find_element(*self.ck1_elem).click()

    def cktrue(self):
        self.driver.find_element(*self.ck_queren1_elem).click()

    def switchdefault(self):
        self.driver.switch_to.default_content()


    def gettext(self):
        return self.driver.find_element(*self.get_text_elem).text

    def gettext1(self):
        return self.driver.find_element(*self.get_tex1_elem).text



