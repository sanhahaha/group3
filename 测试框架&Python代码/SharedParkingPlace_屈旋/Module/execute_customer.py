from FrameDemo.wntest.Tool.fileuite import file_Uite
from FrameDemo.wntest.test_case.test_customer import customer_cases
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

    def start_customer_cases(self):
        logger = self.get_logger(
            os.path.join(
                os.getcwd(),
                'customer_cases'))
        l01 = customer_cases().customer_01()
        l01_expect = int(1)
        if l01 is l01_expect:
            a1 = 'customer_01:断言成功'
            logger.info(a1)
            print(a1)
        else:
            b1 = 'customer_01:断言失败'
            logger.info(b1)
            print(b1)
        self.driver.refresh()

        logger = self.get_logger(
            os.path.join(
                os.getcwd(),
                'customer_query_01'))
        l02 = customer_cases().customer_query_01()
        l02_expect = int(1)
        if l02 is l02_expect:
            a1 = 'customer_01:断言成功'
            logger.info(a1)
            print(a1)
        else:
            b1 = 'customer_01:断言失败'
            logger.info(b1)
            print(b1)
        self.driver.refresh()

        logger = self.get_logger(
            os.path.join(
                os.getcwd(),
                'customer_edit_01'))
        l03 = customer_cases().customer_edit_01()
        l03_expect = int(1)
        if l03 is l03_expect:
            a1 = 'customer_01:断言成功'
            logger.info(a1)
            print(a1)
        else:
            b1 = 'customer_01:断言失败'
            logger.info(b1)
            print(b1)

if __name__ == '__main__':
    obj = execute_login()
    obj.start_customer_cases()