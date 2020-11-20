import time
import unittest

class TestUnitTest_Cases(
        unittest.TestCase):  # unittest框架的测试用例，需要继承unittest.TestCase
    @classmethod
    def setUpClass(cls):   # 类前置方法 类方法只执行一次

        print("测试开始")

    def test_tc1(self):
        print("测试1")

    def test_tc2(self):
        print("测试2")

    def test_tc3(self):
        print("测试3")

    def test_tc4(self):
        print("测试4")

    @classmethod
    def tearDownClass(cls):
        print("测试结束")
