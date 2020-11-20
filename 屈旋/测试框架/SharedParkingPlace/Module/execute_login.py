from FrameDemo.wntest.Tool.fileuite import file_Uite
from FrameDemo.wntest.test_case.test_login import login_cases
from FrameDemo.wntest.Tool.gui_util import uiutil
import os
import logging  # 生成日志
import time


class execute_login:
    def __init__(self):
        self.logger = None
        self.driver = uiutil.get_driver()
        self.data = file_Uite.readfile('..\\config\\test_info.ini', 'login')
        self.loginout = file_Uite.get_ini_value(
            '..\\config\\test_info.ini', 'login', 'loginout')
        '''
        1 = True
        0 = False
        '''

    def get_logger(self, name):
        '''
            生成日志文件
            信息级别：debug,info,warn,error

        '''

        get_time = time.strftime('%Y%m%d_%H%M%S', time.localtime())
        if self.logger is None:
            self.logger = logging.getLogger(name)  # 获取日志生成器对象
            self.logger.setLevel(level=logging.INFO)  # 定义获取信息的级别

            if not os.path.exists('..\\report'):  # 如果目录文件并不存在则创建
                os.mkdir('..\\report')
            handler = logging.FileHandler(
                '..\\report\\' + get_time + '.log',
                encoding='utf8')  # 创建loggger的文件句柄与规定的文件关联
            # 定义信息的格式 系统 模块  等级信息 具体打印的信息
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)  # 收集信息
            self.logger.addHandler(handler)  # 添加信息
            self.logger.info(
                '*****************************************************\n')
        return self.logger

    def start_login(self):
        logger = self.get_logger(
            os.path.join(
                os.getcwd(),
                'start_login'))
        l01 = login_cases().login_01()
        l01_expect = self.data[0]['expect']
        if l01 is l01_expect:
            a1 = 'login_01:断言成功'
            logger.info(a1)
            print(a1)
        else:
            b1 = 'login_01:断言失败'
            logger.info(b1)
            print(b1)
        loginout = self.loginout
        login_loginout = self.driver.find_element_by_xpath(
            loginout)
        uiutil.click(login_loginout)

        l02 = login_cases().login_02()
        l02_expect = self.data[1]['expect']
        if l02 is l02_expect:
            a2 = 'login_02:断言成功'
            logger.info(a2)
            print(a2)
        else:
            b2 = 'login_02:断言失败'
            logger.info(b2)
            print(b2)
        self.driver.refresh()

        l03 = login_cases().login_03()
        l03_expect = self.data[2]['expect']
        if l03 is l03_expect:
            a3 = 'login_03:断言成功'
            logger.info(a3)
            print(a3)
        else:
            b3 = 'login_03:断言失败'
            logger.info(b3)
            print(b3)
        self.driver.refresh()

        l04 = login_cases().login_04()
        l04_expect = self.data[3]['expect']
        if l04 is l04_expect:
            a4 = 'login_04:断言成功'
            logger.info(a4)
            print(a4)
        else:
            b4 = 'login_04:断言失败'
            logger.info(b4)
            print(b4)
        self.driver.refresh()

        l05 = login_cases().login_05()
        l05_expect = self.data[4]['expect']
        if l05 is l05_expect:
            a5 = 'login_05:断言成功'
            logger.info(a5)
            print(a5)
        else:
            b5 = 'login_05:断言失败'
            logger.info(b5)
            print(b5)
        self.driver.refresh()

        l06 = login_cases().login_06()
        l06_expect = self.data[5]['expect']
        if l06 is l06_expect:
            a6 = 'login_06:断言成功'
            logger.info(a6)
            print(a6)
        else:
            b6 = 'login_06:断言失败'
            logger.info(b6)
            print(b6)
        self.driver.refresh()

        l07 = login_cases().login_07()
        l07_expect = self.data[6]['expect']
        if l07 is l07_expect:
            a7 = 'login_07:断言成功'
            logger.info(a7)
            print(a7)
        else:
            b7 = 'login_07:断言失败'
            logger.info(b7)
            print(b7)
        self.driver.refresh()

        l08 = login_cases().login_08()
        l08_expect = self.data[7]['expect']
        if l08 is l08_expect:
            a8 = 'login_08:断言成功'
            logger.info(a8)
            print(a8)
        else:
            b8 = 'login_08:断言失败'
            logger.info(b8)
            print(b8)
        self.driver.quit()


if __name__ == '__main__':
    obj = execute_login()
    obj.start_login()
