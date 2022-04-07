# encoding: utf-8
'''
@author: xxx
@file: test_create_photo.py
@time: 2022-04-01 15:46
@desc:
'''
import time
import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from iwebsns.config.config import *
from iwebsns.object.login_object import *
from iwebsns.data.login_data import *
from iwebsns.object.create_photo_object import *


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
        cls.createphoto = CreatePhoto(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        '''
        关闭浏览器
        :return:
        '''
        cls.driver.quit()

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

    def test_001(self):
        '''
        创建相册
        :return:
        '''
        value_list = Datas().read_excel('创建相册')
        key1 = value_list[0][0]
        key2 = value_list[0][1]
        key3 = value_list[0][2]
        self.createphoto.ckphoto()
        self.createphoto.sendname1(key1)
        self.createphoto.sendname2(key2)
        self.createphoto.sendname3(key3)
        self.createphoto.cktrue()
        self.createphoto.ckmyphoto()
        time.sleep(1)
        try:
            self.assertEqual(key1, self.createphoto.gettext())
            print('创建相册成功')
        except:
            print('创建相册失败')


    def test_002(self):
        '''
        名称和描述为空创建相册
        :return:
        '''
        self.createphoto.ckphoto()
        self.createphoto.cktrue()
        self.createphoto.swdefault()
        try:
            self.assertEqual('请正确填入相册名和描述！', self.createphoto.gettext1())
            print('弹出填写提示成功')
        except:
            print('弹出填写提示失败')
        self.createphoto.cktrue1()

    def test_003(self):
        '''
        描述为空创建相册
        :return:
        '''
        self.createphoto.ckphoto()
        value_list = Datas().read_excel('创建相册')
        key1 = value_list[0][0]
        self.createphoto.sendname1(key1)
        self.createphoto.cktrue()
        self.createphoto.swdefault()
        try:
            self.assertEqual('请正确填入相册名和描述！', self.createphoto.gettext1())
            print('弹出填写提示成功')
        except:
            print('弹出填写提示失败')
        self.createphoto.cktrue1()



if __name__ == '__main__':
    unittest.main()
