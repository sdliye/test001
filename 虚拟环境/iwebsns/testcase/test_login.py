# encoding: utf-8
'''
@author: xxx
@file: test_login.py
@time: 2022-03-31 13:54
@desc:
'''
import time
import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from iwebsns.config.config import *
from iwebsns.object.login_object import *
from iwebsns.data.login_data import *


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

    @classmethod
    def tearDownClass(cls) -> None:
        '''
        关闭浏览器
        :return:
        '''
        cls.driver.quit()

    def test001(self):
        '''
        验证登陆成功
        :return:
        '''
        value_list = Datas().read_excel('登录')
        username = value_list[0][0]
        password = value_list[0][1]
        self.login.user_paswd(username, password)
        time.sleep(1)
        try:
            self.assertEqual('我的主页', self.login.gettest())
            print('登录成功')
        except:
            print('登录失败')

        self.login.exit()
        time.sleep(1)

        try:
            self.assertIn(self.driver.title, '聚易社区')
            print('退出成功')
        except:
            print('退出失败')

    def test002(self):
        '''
        验证密码为空登录
        :return:
        '''
        value_list = Datas().read_excel('登录')
        username = value_list[1][0]
        password = value_list[1][1]
        self.login.user_paswd02(username)
        time.sleep(1)
        try:
            self.assertEqual('密码不能为空!', self.login.gettest01())
            print('空密码提示弹出成功')
        except:
            print('空密码提示弹出成功失败')

    def test003(self):
        '''
        验证密码为空格登录
        :return:
        '''
        value_list = Datas().read_excel('登录')
        username = value_list[2][0]
        self.login.user_paswd03(username,)
        time.sleep(1)
        try:
            self.assertEqual('用户密码错误!', self.login.gettest01())
            print('空格密码提示弹出成功')
        except:
            print('空格密码提示弹出成功')

    def test004(self):
        '''
        验证账号为空登录
        :return:
        '''
        value_list = Datas().read_excel('登录')
        password = value_list[3][1]
        self.login.user_paswd04(password)
        time.sleep(1)
        try:
            self.assertEqual('登录帐号错误，请重试', self.login.gettest02())
            print('空账号提示弹出成功')
        except:
            print('空账号提示弹出成功')

    def test005(self):
        '''
        验证账号为空格登录
        :return:
        '''
        value_list = Datas().read_excel('登录')
        password = value_list[4][1]
        self.login.user_paswd05(password)
        time.sleep(1)
        try:
            self.assertEqual('登录帐号错误，请重试', self.login.gettest02())
            print('空格账号提示弹出成功')
        except:
            print('空格账号提示弹出成功')

    def test006(self):
        '''
        验证错误账号登录
        :return:
        '''
        value_list = Datas().read_excel('登录')
        username = value_list[5][0]
        password = value_list[5][1]
        self.login.user_paswd(username, password)
        time.sleep(1)
        try:
            self.assertEqual('登录帐号错误，请重试', self.login.gettest02())
            print('错误账号提示弹出成功')
        except:
            print('错误账号提示弹出成功')

    def test007(self):
        '''
        验证错误密码登录
        :return:
        '''
        value_list = Datas().read_excel('登录')
        username = value_list[6][0]
        password = value_list[6][1]
        self.login.user_paswd(username, password)
        time.sleep(1)
        try:
            self.assertEqual('用户密码错误!', self.login.gettest01())
            print('错误密码提示弹出成功')
        except:
            print('错误密码提示弹出成功')




if __name__ == '__main__':
    unittest.main()
