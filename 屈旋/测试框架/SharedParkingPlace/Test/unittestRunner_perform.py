import time
import unittest
from FrameDemo.SharedParkingPlace.Test.test_api_case import TestUnitTest_Api_Cases
from HTMLTestRunner_cn import HTMLTestRunner

class UnittestPerform:
    def perform(self):
        # 测试用例从哪来 到哪去
        # 用例从TestLoader到套件，到执行，最后生成报告
        test_suite = unittest.TestSuite()
        tc01 = unittest.TestLoader().loadTestsFromTestCase(TestUnitTest_Api_Cases)  # 加载要执行的用例
        # 将用例放入测试套件中

        test_suite.addTest(tc01)  # 将装载用例放入测试套件中
        # 实例化一个执行器，最后调用执行的run方法
        now = time.strftime("%Y-%m-%d_%H%M%S")  # 定义一个时间字符串，准备用来做测试报告的名字
        file_name = "../Report/" + now + "report.html"
        fp = open(file_name, "wb") # 写入文件使用二进制的格式
        runner = HTMLTestRunner(stream=fp, verbosity=2, title="37期自动化测试报告", tester="37期")
        runner.run(test_suite)
        fp.close()


if __name__ == '__main__':
    testperform =UnittestPerform()
    testperform.perform()
