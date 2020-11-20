from woniutestV1.tools.lib_util import UiUtil


class Login:

    def __init__(self, driver):
        self.driver = driver

    def input_account(self, username):
        uname = UiUtil.find_elment('login','uname')
        UiUtil.input(uname, username)

    def input_password(self, password):
        upass = UiUtil.find_elment('login','upass')
        UiUtil.input(upass, password)

    def input_verifycode(self, verifycode):
        vfcode = UiUtil.find_elment('login','vfcode')
        UiUtil.input(vfcode, verifycode)

    def click_login_button(self):
        login_button = UiUtil.find_elment('login','login_button')
        UiUtil.click(login_button)

    def do_login(self, login_data):
        self.input_account(login_data['username'])
        self.input_password(login_data['password'])
        self.input_verifycode(login_data['verifycode'])
        self.click_login_button()

    #完成登录后需不需要点击注销；如果点击了怎么进行判断页面元素，



if __name__ == '__main__':
    driver = UiUtil.get_driver()
    login_data = {'username':'admin', 'password':'Milor123', 'verifycode':'0000'}
    Login(driver).do_login(login_data)
