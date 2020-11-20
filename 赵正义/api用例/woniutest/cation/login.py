import time

from woniutest.ui_util.web_ui import UiUtil


class  Login:
    def  __init__(self,driver):

        self.driver = driver



    def input_username(self,username):
        name = self.driver.find_element_by_id("username")
        UiUtil.input(name,username)

    def input_password(self, password):
        ps = self.driver.find_element_by_id("password")
        UiUtil.input(ps, password)

    def input_verifycode(self,verifycode):
        vf = self.driver.find_element_by_id("verifycode")
        UiUtil.input(vf,verifycode)

    def click_login(self):
        login_button = self.driver.find_element_by_css_selector("button.form-control")
        UiUtil.click(login_button)


    def logout(self):
        ele=self.driver.find_element_by_xpath('//*[text()="注销"]')
        UiUtil.click(ele)
    def ok(self):
        time.sleep(0.2)
        self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[3]/button').click()
        # ele=self.driver.find_element_by_xpath('//*[text()="ok"]')
        # time.sleep(0.5)
        # UiUtil.click(ele)
    def do_login(self,login_data):
        self.input_username(login_data["username"])
        self.input_password(login_data["password"])
        self.input_verifycode(login_data["verifycode"])
        self.click_login()