import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class CreateFenlei:
    def __init__(self, driver):
        self.driver = driver
        self.ck_log_elem = By.LINK_TEXT, '日志'
        self.frame1_elem = 'frame_content'
        self.ck_cr_log_elem = By.LINK_TEXT, '新建日志'
        self.ck_add_elem = By.LINK_TEXT, '添加分类'
        self.inp_name1_elem = By.ID, 'new_sort_name'
        self.ck_save_elem = By.CLASS_NAME, 'small-btn'
        self.get_text_elem = By.XPATH, '/html[1]/body[1]/form[1]/table[1]/tbody[1]/tr[2]/td[1]' \
                                       '/table[1]/tbody[1]/tr[1]/td[1]/div[1]/select[1]'
        self.get_text1_elem=By.ID,'Message_undefined'
        self.tip_elem=By.ID,'Message_undefined'
        self.ck_true_elem=By.ID,'_ButtonCancel_0'


    def into_log(self):
        self.driver.find_element(*self.ck_log_elem).click()
        time.sleep(1)
        self.driver.switch_to.frame(self.frame1_elem)
        self.driver.find_element(*self.ck_cr_log_elem).click()
        time.sleep(1)
        self.driver.find_element(*self.ck_add_elem).click()

    def add_fenlei(self, key1):
        self.driver.find_element(*self.inp_name1_elem).send_keys(key1)
        time.sleep(1)

    def addfenlei1(self):
        self.driver.find_element(*self.inp_name1_elem).send_keys(Keys.SPACE)

    def cktrue(self):
        self.driver.find_element(*self.ck_save_elem).click()

    def swdefault(self):
        self.driver.switch_to.default_content()

    def tiptrue(self):
        self.driver.find_element(*self.ck_true_elem).click()

    def gettext(self):
        return self.driver.find_element(*self.get_text_elem).text

    def gettext1(self):
        return self.driver.find_element(*self.get_text1_elem).text
