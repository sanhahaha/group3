from FrameDemo.wntest.Tool.gui_util import uiutil

class startmethod:
    def __init__(self):
        self.driver = uiutil.get_driver()

    def do_add_customer(self,username,password,verifycode):
        '''
        不使用
        :param username:
        :param password:
        :param verifycode:
        :return:
        '''

        uname = self.driver.find_element_by_id('username')
        uiutil.input(uname,username)
        upass = self.driver.find_element_by_id('password')
        uiutil.input(upass,password)
        vfcode = self.driver.find_element_by_id('verifycode')
        uiutil.input(vfcode,verifycode)
        login_button = self.driver.find_element_by_css_selector('button.form-control')
        uiutil.click(login_button
                     )

    def do_query_customer(self):
        pass

    def start_login(self):
        '''
        start
        :return:
        '''
        from FrameDemo.wntest.Tool.fileuite import file_Uite
        from FrameDemo.wntest.action import login
        username = file_Uite.get_ini_value('..\\config\\base.ini', 'login', 'username')
        password = file_Uite.get_ini_value('..\\config\\base.ini', 'login', 'password')
        verifycode = file_Uite.get_ini_value('..\\config\\base.ini', 'login', 'verifycode')
        login.Login(uiutil.get_driver()).do_login(username, password, verifycode)



if __name__ == '__main__':
    obj = startmethod()
    obj.start_login()