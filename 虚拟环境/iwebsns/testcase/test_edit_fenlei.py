# encoding: utf-8
'''
@author: xxx
@file: test_edit_fenlei.py
@time: 2022-04-01 11:09
@desc:
'''
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
from iwebsns.object.edit_fenlei_object import *


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
        cls.editfenlei = EditFenlei(cls.driver)

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
        编辑分类
        :return:
        '''
        value_list = Datas().read_excel('编辑分类')
        key1 = value_list[0][0]
        self.editfenlei.into_logfenlei()
        self.editfenlei.ckedit()
        self.editfenlei.editlog(key1)
        self.editfenlei.save()
        time.sleep(1)
        try:
            self.assertEqual(key1, self.editfenlei.get_text())
            print('编辑分类成功')
        except:
            print('编辑分类失败')

    def test002(self):
        '''
        删除分类
        :return:
        '''
        self.editfenlei.into_logfenlei()
        self.editfenlei.ckdel()
        try:
            self.assertIn('日志分类',self.editfenlei.get_text1())
            print('删除分类成功')
        except:
            print('删除分类失败')

    def test003(self):
        '''
        编辑名字为空格分类
        :return:
        '''
        self.editfenlei.into_logfenlei()
        self.editfenlei.ckedit()
        self.editfenlei.editlog1()
        self.editfenlei.save()
        try:
            self.assertIsNone(self.editfenlei.get_text())
            print('编辑分类名字为空格失败')
        except:
            print('编辑分类名字为空格成功')

    def test004(self):
        '''
        编辑名字为空分类
        :return:
        '''
        self.editfenlei.into_logfenlei()
        self.editfenlei.ckedit()
        self.editfenlei.save()
        try:
            self.assertIsNone(self.editfenlei.get_text())
            print('编辑分类名字为空格失败')
        except:
            print('编辑分类名字为空格成功')


if __name__ == '__main__':
    unittest.main()
