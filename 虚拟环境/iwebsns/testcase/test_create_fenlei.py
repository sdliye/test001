# encoding: utf-8
'''
@author: xxx
@file: test_create_log.py
@time: 2022-03-31 15:40
@desc:
'''

import time
import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from iwebsns.config.config import *
from iwebsns.object.login_object import *
from iwebsns.data.login_data import *
from iwebsns.object.create_fenlei_object import CreateFenlei


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
        cls.createfenelei = CreateFenlei(cls.driver)

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

    def tearDown(self) -> None:
        '''
        退出
        :return:
        '''
        self.login.exit()

    def test001(self):
        '''
        创建分类
        :return:
        '''
        value_list = Datas().read_excel('创建分类')
        key1 = value_list[0][0]
        self.createfenelei.into_log()
        self.createfenelei.add_fenlei(key1)
        self.createfenelei.cktrue()
        time.sleep(1)
        str = self.createfenelei.gettext()
        list1 = str.split('\n')
        try:
            self.assertEqual(key1, list1[1])
            print('创建分类成功')
        except:
            print('创建分类失败')

    def test002(self):
        '''
        创建名字为空分类
        :return:
        '''
        self.createfenelei.into_log()
        self.createfenelei.cktrue()
        self.createfenelei.swdefault()
        try:
            self.assertEqual('请填写信息',self.createfenelei.gettext1())
            print('名字为空分类弹出提示成功')
        except:
            print('名字为空分类弹出提示失败')
        self.createfenelei.tiptrue()

    def test003(self):
        '''
        创建名字为空格分类
        :return:
        '''
        self.createfenelei.into_log()
        self.createfenelei.addfenlei1()
        self.createfenelei.cktrue()
        self.createfenelei.swdefault()
        try:
            self.assertEqual('请填写信息',self.createfenelei.gettext1())
            print('名字为空格分类弹出提示成功')
        except:
            print('名字为空格分类弹出提示失败')

        self.createfenelei.tiptrue()



if __name__ == '__main__':
    unittest.main()
