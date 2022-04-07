# encoding: utf-8
'''
@author: xxx
@file: test_create_group.py
@time: 2022-04-02 16:05
@desc:
'''
import time
import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from iwebsns.config.config import *
from iwebsns.object.login_object import *
from iwebsns.data.login_data import *
from iwebsns.object.create_group_object import CreateGroup


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
        cls.creategroup = CreateGroup(cls.driver)

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

    def test_001(self):
        '''
        创建群组
        turn:
        '''
        value_list = Datas().read_excel('创建群组')
        key1 = value_list[0][0]
        key2 = value_list[0][1]
        choise1 = value_list[0][2]
        key3=value_list[0][3]
        choise2=value_list[0][4]

        self.creategroup.creategoup()
        time.sleep(1)
        self.creategroup.inpkey(key1,key2,choise1,key3,choise2,photo_path)
        self.creategroup.ckcreate()
        try:
            self.assertEqual(key1,self.creategroup.gettext())
            print('创建群组成功')
        except:
            print('创建群组失败')

    def test_002(self):
        '''
        全为空创建群组
        turn:
        '''
        self.creategroup.creategoup()
        time.sleep(1)
        self.creategroup.ckcreate()
        self.creategroup.switchdefault()
        try:
            self.assertEqual('请认真填写每个选项', self.creategroup.gettext1())
            print('弹出提示成功')
        except:
            print('弹出提示失败')
        self.creategroup.cktrue()

if __name__ == '__main__':
    unittest.main()


