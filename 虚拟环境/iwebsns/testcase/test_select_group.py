# encoding: utf-8
'''
@author: xxx
@file: test_select_group.py
@time: 2022-04-05 12:44
@desc:
'''
import time
import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from iwebsns.config.config import *
from iwebsns.object.login_object import *
from iwebsns.data.login_data import *
from iwebsns.object.select_group_object import SelectGroup


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        '''
        打开浏览器
        :return:
        '''
        e = Service(executable_path=driver_path)
        cls.driver = webdriver.Edge(service=e)
        cls.driver.maximize_window()
        cls.driver.get(url)
        cls.login = LoginPage(cls.driver)
        cls.selectgroup = SelectGroup(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        '''
        关闭浏览器
        :return:
        '''
        cls.driver.quit()
        # pass

    def setUp(self) -> None:
        '''
        登录
        :return:
        '''
        value_list = Datas().read_excel('登录')
        username = value_list[0][0]
        password = value_list[0][1]
        self.login.user_paswd(username, password)
        time.sleep(1)

    def test_001(self):
        '''
        创建群组
        turn:
        '''
        value_list = Datas().read_excel('搜索群组')
        key1 = value_list[0][0]
        key2 = value_list[0][1]
        choise = value_list[0][2]

        self.selectgroup.intogroup()
        time.sleep(1)
        self.selectgroup.selectgroup(key1,key2,choise)
        try:
            self.assertEqual(key1,self.selectgroup.gettext())
            print('搜索正确')
        except:
            print('搜索失败')

if __name__=='__main__':
    unittest.main()