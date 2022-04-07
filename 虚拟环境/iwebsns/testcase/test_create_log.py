# encoding: utf-8
'''
@author: xxx
@file: test_create_log.py
@time: 2022-03-31 15:40
@desc:
'''
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
from iwebsns.object.create_log_object import *


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
        cls.crlog = CreateLog(cls.driver)

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
        创建日志
        :return:
        '''
        values_list = Datas().read_excel('创建日志')
        key1 = values_list[0][0]
        key2 = values_list[0][1]
        key3 = values_list[0][2]
        key4 = values_list[0][3]
        self.crlog.create_log()
        self.crlog.send_key1(key1)
        self.crlog.send_key2(key2)
        self.crlog.choiceclassify(key4)
        self.crlog.send_key3(key3)
        self.crlog.setscrall()
        self.crlog.ck_quren()
        time.sleep(1)

        try:
            self.assertEqual(key1, self.crlog.gettext())
            print('创建日志成功')
        except:
            print('创建日志失败')

    def test_002(self):
        '''
        全为空创建日志(验证必填项标题)
        :return:
        '''
        self.crlog.create_log()
        self.crlog.setscrall()
        self.crlog.ck_quren()
        self.crlog.switchdefault()
        try:
            self.assertEqual('请填写标题', self.crlog.gettext02())
            print('弹出填写标题提示成功')
        except:
            print('弹出填写标题提示失败')
        self.crlog.ck_quren02()

    def test_003(self):
        '''
        只填标题创建日志(验证必填项内容)
        :return:
        '''
        values_list = Datas().read_excel('创建日志')
        key1 = values_list[0][0]
        self.crlog.create_log()
        self.crlog.send_key1(key1)
        self.crlog.setscrall()
        self.crlog.ck_quren()
        time.sleep(1)
        self.crlog.switchdefault()
        try:
            self.assertEqual('请填写内容', self.crlog.gettext02())
            print('弹出填写内容提示成功')
        except:
            print('弹出填写内容提示失败')
        self.crlog.ck_quren02()







if __name__ == '__main__':
    unittest.main()
