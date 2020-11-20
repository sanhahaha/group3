import time
import unittest
from HTMLTestRunner_cn import HTMLTestRunner
from Shared_Parking.test_case.test_login_api import TestLoginAPI

class UnittestPerform:
    def perform(self):
        test_suite = unittest.TestSuite()
        tc01 = unittest.TestLoader().loadTestsFromTestCase(TestLoginAPI)  # 加载要执行的用例
        test_suite.addTest(tc01)                                          # 将用例放入测试套件中

        # 实例化一个执行器，最后调用执行的run方法
        now = time.strftime("%Y-%m-%d_%H%M%S")  # 定义一个时间字符串，准备用来做测试报告的名字
        file_name = "../report/" + now + "report.html"
        fp = open(file_name, "wb") # 写入文件使用二进制的格式
        runner = HTMLTestRunner(stream=fp, verbosity=2, title="37期自动化测试报告", tester="37期")
        runner.run(test_suite)
        fp.close()


if __name__ == '__main__':
    testperform =UnittestPerform()
    testperform.perform()
