from woniutest.tool.util import FileUtil
from woniutest.ui_util.web_ui import UiUtil


class Login:

    def __init__(self, driver):

        self.driver = driver

    def input_account(self, username):

        uname_element = UiUtil.find_elment('login', 'uname')
        UiUtil.input(uname_element, username)

    def input_password(self, password):
        upass_element = UiUtil.find_elment('login', 'upass')
        UiUtil.input(upass_element, password)

    def input_verifycode(self, verifycode):
        vfcode_element = UiUtil.find_elment('login', 'vfcode')
        UiUtil.input(vfcode_element, verifycode)

    def click_login_button(self):
        login_button_element = UiUtil.find_elment('login', 'login_button')
        UiUtil.click(login_button_element)

    def do_login(self, login_data):
        self.input_account(login_data['username'])
        self.input_password(login_data['password'])
        self.input_verifycode(login_data['verifycode'])
        self.click_login_button()


if __name__ == '__main__':
    driver = UiUtil.get_driver()
    data=FileUtil.get_excel("../conf/woniu.json", 0)
    print(data[0])
    Login(driver).do_login(data[0])
