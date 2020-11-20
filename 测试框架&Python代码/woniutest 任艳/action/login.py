from pycharm.测试框架.woniutestV1.tools.lib_util import UiUtil
import time

# from woniutest.presentation.demo03 import GetDriver  #图像识别工具
from pycharm.测试框架.woniutestV1.tools.lib_util import Assert #动作断言
class Login:
    def _init__(self,driver):
        self.driver = driver
    def input_account( self,username) :
        uname = self.driver.find_element_by_id('username')
        UiUtil().input(uname,username)

    def input_password( self,password):
        upass = self.driver.find_element_by_id('password')
        UiUtil().input(upass,password)
    def input_verifycode( self,verifycode):
        vfcode = self.driver.find_element_by_id('verifycode')
        UiUtil().input(vfcode,verifycode)

    def click_login_button(self): #登录
        login_button = self.driver.find_element_by_css_selector('button.form-control')
        login_button.click()

    def do_login(self,username,password,verifycode):
        self.input_account(username)
        self.driver.implicitly_wait(1)
        self.input_password(password)
        self.driver.implicitly_wait(1)
        self.input_verifycode(verifycode)
        self.driver.implicitly_wait(1)
        self.click_login_button()
        time.sleep(1)
if __name__ == '__main__':
     test =UiUtil.get_driver("Chrome")
     u=test.Login()
     u.do_login("admin","Milor123","0000")