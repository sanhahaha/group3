
from FrameDemo.SharedParkingPlace.Tool.gui_util import uiutil
from FrameDemo.SharedParkingPlace.Tool.file_uite import File_Uite



class login:
    def __init__(self,driver):
        self.driver = driver

    def input_account(self, username):
        uname_element = uiutil.find_element('login', 'uname')
        uiutil.input(uname_element, username)

    def input_password(self, password):
        upass_element = uiutil.find_element('login', 'upass')
        uiutil.input(upass_element, password)

    def input_verifycode(self, verifycode):
        vfcode_element = uiutil.find_element('login', 'vfcode')
        uiutil.input(vfcode_element, verifycode)

    def click_login_button(self):
        login_button_element = uiutil.find_element('login', 'login_button')
        uiutil.click(login_button_element)

    def do_login(self, username, password,verifycode):
        self.input_account(username)
        self.input_password(password)
        self.input_verifycode(verifycode)
        self.click_login_button()

if __name__ == '__main__':
    # from selenium import webdriver
    driver = uiutil().get_driver()

