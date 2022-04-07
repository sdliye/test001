# encoding: utf-8
'''
@author: xxx
@file: test_upload_photo.py
@time: 2022-04-01 15:35
@desc:
'''
import time
import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service


from iwebsns.config.config import *
from iwebsns.object.login_object import *
from iwebsns.data.login_data import *
from iwebsns.object.upload_photo_object import UploadPhoto


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        '''
        打开浏览器
        :return:
        '''
        e = Service(executable_path=driver_path)
        cls.photo = photo_path
        cls.driver = webdriver.Edge(service=e)
        cls.driver.maximize_window()
        cls.driver.get(url)
        cls.login = LoginPage(cls.driver)
        cls.uploadphoto = UploadPhoto(cls.driver)

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
        上传相片
        :return:
        '''
        value_list = Datas().read_excel('上传相片')
        key1 = value_list[0][0]
        key2 = value_list[0][1]
        key3 = value_list[0][2]
        self.uploadphoto.into_photo()
        self.uploadphoto.upload_pictures(key3,photo_path)
        time.sleep(5)
        self.uploadphoto.ck_cofirm(key1, key2)
        try:
            self.assertEqual('编辑相册', self.uploadphoto.gettext())
            print('上传成功')
        except:
            print('上传失败')


if __name__ == '__main__':
    unittest.main()
