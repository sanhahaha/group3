from FrameDemo.wntest.test_case import test_login
from FrameDemo.wntest.test_case import test_customer
from FrameDemo.wntest.execute_case.ddt_ui_startup import TestUnitTest_Cases
from FrameDemo.wntest.Tool.fileuite import file_Uite
from HTMLTestRunner_cn import HTMLTestRunner
import time
import unittest

class UnittestPerform:
    def perform(self):
        # 测试用例从哪来 到哪去
        # 用例从TestLoader到套件，到执行，最后生成报告
        test_suite = unittest.TestSuite()
        tc01 = unittest.TestLoader().loadTestsFromTestCase(TestUnitTest_Cases)  # 加载要执行的用例
        # 将用例放入测试套件中

        test_suite.addTest(tc01)  # 将装载用例放入测试套件中
        # 实例化一个执行器，最后调用执行的run方法
        now = time.strftime("%Y-%m-%d_%H%M%S")  # 定义一个时间字符串，准备用来做测试报告的名字
        file_name = "../report/" + "ui自动化报告" + now + "report.html"
        fp = open(file_name, "wb") # 写入文件使用二进制的格式
        runner = HTMLTestRunner(stream=fp, verbosity=2, title="自动化测试报告", tester="ui")
        runner.run(test_suite)
        fp.close()


if __name__ == '__main__':
    testperform =UnittestPerform()
    testperform.perform()
