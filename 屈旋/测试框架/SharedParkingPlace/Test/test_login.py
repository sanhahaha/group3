from FrameDemo.wntest.Tool.gui_util import uiutil
from FrameDemo.wntest.Tool.fileuite import file_Uite
from FrameDemo.wntest.Tool.fileuite import loguti1
from FrameDemo.wntest.action import login
import os


class login_cases:
    def __init__(self):
        self.driver = uiutil.get_driver()
        self.data = file_Uite.readfile('..\\config\\test_info.ini', 'login')
        self.loginpass = file_Uite.get_ini_value(
            '..\\config\\test_info.ini', 'login', 'loginpass')
        self.loginfail = file_Uite.get_ini_value(
            '..\\config\\test_info.ini', 'login', 'loginfail')
        self.loginverifyfail = file_Uite.get_ini_value(
            '..\\config\\test_info.ini', 'login', 'loginverifyfail')

    def login_01(self):
        '''
        验证是否登录成功

        1 = True
        0 = False
        :return:
        '''
        logger = loguti1.get_logger(
            os.path.join(
                os.getcwd(),
                'login_case_01'))   # 获得日志生成器对象
        try:
            username = self.data[0]['username']
            password = self.data[0]['password']
            verifycode = self.data[0]['verifycode']
            login.Login(
                uiutil.get_driver()).do_login(
                username,
                password,
                verifycode)
            logger.info('login_01读取正确')
            login_pass = self.loginpass
            login_passverif = self.driver.find_element_by_xpath(
                login_pass).text

            if "admin   管理员" in login_passverif:
                print('用户登录成功，元素存在')
                return int(1)
            else:
                print('用户登录失败，元素不存在')
                return int(0)
        except BaseException:
            logger.error('login_01读取错误')
            return int(0)
        finally:
            print('login_01''执行完毕')

    def login_02(self):
        logger = loguti1.get_logger(
            os.path.join(
                os.getcwd(),
                'login_case_02'))  # 获得日志生成器对象
        try:
            username = self.data[1]['username']
            password = self.data[1]['password']
            verifycode = self.data[1]['verifycode']
            login.Login(
                uiutil.get_driver()).do_login(
                username,
                password,
                verifycode)
            logger.info('login_02读取正确')
            login_loginfail = self.loginfail
            login_login_loginfail = self.driver.find_element_by_xpath(
                login_loginfail).text
            if "登录失败，请重新登录." in login_login_loginfail:
                print('验证用户登录失败.成功，元素存在')
                return int(1)
            else:
                print('验证用户登录失败.失败，元素不存在')
                return int(0)

        except BaseException:
            logger.error('login_02读取错误')
            return int(0)
        finally:
            print('login_02''执行完毕')

    def login_03(self):
        logger = loguti1.get_logger(
            os.path.join(
                os.getcwd(),
                'login_case_03'))  # 获得日志生成器对象
        try:
            username = self.data[2]['username']
            password = self.data[2]['password']
            verifycode = self.data[2]['verifycode']
            login.Login(
                uiutil.get_driver()).do_login(
                username,
                password,
                verifycode)
            logger.info('login_03读取正确')
            login_loginfail = self.loginfail
            login_login_loginfail = self.driver.find_element_by_xpath(
                login_loginfail).text
            if "登录失败，请重新登录." in login_login_loginfail:
                print('验证用户登录失败.成功，元素存在')
                return int(1)
            else:
                print('验证用户登录失败.失败，元素不存在')
                return int(0)
        except BaseException:
            logger.error('login_03读取错误')
            return int(0)
        finally:
            print('login_03''执行完毕')

    def login_04(self):
        logger = loguti1.get_logger(
            os.path.join(
                os.getcwd(),
                'login_case_04'))  # 获得日志生成器对象
        try:
            username = self.data[3]['username']
            password = self.data[3]['password']
            verifycode = self.data[3]['verifycode']
            login.Login(
                uiutil.get_driver()).do_login(
                username,
                password,
                verifycode)
            logger.info('login_04读取正确')
            login_loginfail = self.loginfail
            login_login_loginfail = self.driver.find_element_by_xpath(
                login_loginfail).text
            if "登录失败，请重新登录." in login_login_loginfail:
                print('验证用户登录失败.成功，元素存在')
                return int(1)
            else:
                print('验证用户登录失败.失败，元素不存在')
                return int(0)
        except BaseException:
            logger.error('login_04读取错误')
            return int(0)
        finally:
            print('login_04''执行完毕')

    def login_05(self):
        logger = loguti1.get_logger(
            os.path.join(
                os.getcwd(),
                'login_case_05'))  # 获得日志生成器对象
        try:
            username = self.data[4]['username']
            password = self.data[4]['password']
            verifycode = self.data[4]['verifycode']
            login.Login(
                uiutil.get_driver()).do_login(
                username,
                password,
                verifycode)
            logger.info('login_05读取正确')
            login_loginfail = self.loginfail
            login_login_loginfail = self.driver.find_element_by_xpath(
                login_loginfail).text
            if "登录失败，请重新登录." in login_login_loginfail:
                print('验证用户登录失败.成功，元素存在')
                return int(1)
            else:
                print('验证用户登录失败.失败，元素不存在')
                return int(0)
        except BaseException:
            logger.error('login_05读取错误')
            return int(0)
        finally:
            print('login_05''执行完毕')

    def login_06(self):
        logger = loguti1.get_logger(
            os.path.join(
                os.getcwd(),
                'login_case_06'))  # 获得日志生成器对象
        try:
            username = self.data[5]['username']
            password = self.data[5]['password']
            verifycode = self.data[5]['verifycode']
            login.Login(
                uiutil.get_driver()).do_login(
                username,
                password,
                verifycode)
            logger.info('login_06读取正确')
            login_loginverifyfail = self.loginverifyfail
            login_login_loginverifyfail = self.driver.find_element_by_xpath(
                login_loginverifyfail).text
            if "验证码失效，请重新输入." in login_login_loginverifyfail:
                print('验证登录失败成功，元素存在')
                return int(1)
            else:
                print('验证登录失败.失败，元素不存在')
                return int(0)
        except BaseException:
            logger.error('login_06读取错误')
            return int(0)
        finally:
            print('login_06''执行完毕')

    def login_07(self):
        logger = loguti1.get_logger(
            os.path.join(
                os.getcwd(),
                'login_case_07'))  # 获得日志生成器对象
        try:
            username = self.data[6]['username']
            password = self.data[6]['password']
            verifycode = self.data[6]['verifycode']
            login.Login(
                uiutil.get_driver()).do_login(
                username,
                password,
                verifycode)
            logger.info('login_07读取正确')
            login_loginfail = self.loginfail
            login_login_loginfail = self.driver.find_element_by_xpath(
                login_loginfail).text
            if "登录失败，请重新登录." in login_login_loginfail:
                print('验证用户登录失败.成功，元素存在')
                return int(1)
            else:
                print('验证用户登录失败.失败，元素不存在')
                return int(0)
        except BaseException:
            logger.error('login_07读取错误')
            return int(0)
        finally:
            print('login_07''执行完毕')

    def login_08(self):
        logger = loguti1.get_logger(
            os.path.join(
                os.getcwd(),
                'login_case_08'))  # 获得日志生成器对象
        try:
            username = self.data[7]['username']
            password = self.data[7]['password']
            verifycode = self.data[7]['verifycode']
            login.Login(
                uiutil.get_driver()).do_login(
                username,
                password,
                verifycode)
            logger.info('login_08读取正确')
            login_loginfail = self.loginfail
            login_login_loginfail = self.driver.find_element_by_xpath(
                login_loginfail).text
            if "登录失败，请重新登录." in login_login_loginfail:
                print('验证用户登录失败.成功，元素存在')
                return int(1)
            else:
                print('验证用户登录失败.失败，元素不存在')
                return int(0)
        except BaseException:
            logger.error('login_08读取错误')
            return int(0)
        finally:
            print('login_08''执行完毕')

    # def login_for(self):
    #     logger = loguti1.get_logger(
    #         os.path.join(
    #             os.getcwd(),
    #             'login_for'))  # 获得日志生成器对象
    #
    #     '''
    #         条件:读取self.data文件的数据  退出条件:len < 9
    #             将读取的数据传进执行体中  : for
    #             根据执行的条件判断       : break
    #
    #     '''
    #     data_len = 0
    #     while (data_len<len(self.data)):
    #             print(data_len)
    #             for data in self.data:
    #                 username = data[0]['username']
    #                 password = data[0]['password']
    #                 verifycode = data[0]['verifycode']
    #                 test = login.Login(uiutil.get_driver()).do_login(username,password,verifycode)
    #
    #                 while True:
    #                     i = 1
    #                     j = 0
    #                     k = 0
    #                     if i is 1:
    #                         loginpass = file_Uite.get_ini_value(
    #                             '..\\config\\test_info.ini', 'login', 'loginpass')
    #                         login_pass = loginpass
    #                         login_passverif = self.driver.find_element_by_xpath(
    #                             login_pass).text
    #                         if "admin   管理员" in login_passverif:
    #                             print('用户登录成功，元素存在')
    #                             j +=1
    #                             continue
    #                         else:
    #                             print('用户登录失败，元素不存在')
    #                             j += 1
    #                             continue
    #
    #
    #                     elif j is 1:
    #                         loginverifyfail = file_Uite.get_ini_value(
    #                             '..\\config\\test_info.ini', 'login', 'loginverifyfail')
    #                         login_loginverifyfail = loginverifyfail
    #                         login_login_loginverifyfail = self.driver.find_element_by_xpath(
    #                             login_loginverifyfail).text
    #                         if "验证码失效，请重新输入." in login_login_loginverifyfail:
    #                             print('验证登录失败成功，元素存在')
    #                             k +=1
    #                             continue
    #                         else:
    #                             print('验证登录失败.失败，元素不存在')
    #                             k += 1
    #                             continue
    #
    #                     elif k is 1:
    #                         self.loginfail = file_Uite.get_ini_value(
    #                             '..\\config\\test_info.ini', 'login', 'loginfail')
    #                         login_loginfail = self.loginfail
    #                         login_login_loginfail = self.driver.find_element_by_xpath(
    #                             login_loginfail).text
    #                         if "登录失败，请重新登录." in login_login_loginfail:
    #                             print('验证用户登录失败.成功，元素存在')
    #                             continue
    #                         else:
    #                             print('验证用户登录失败.失败，元素不存在')
    #                             continue
    #
    #                 break
    #
    #
    #             data_len +=1


if __name__ == '__main__':
    obj = login_cases()
    print(obj.login_01())
