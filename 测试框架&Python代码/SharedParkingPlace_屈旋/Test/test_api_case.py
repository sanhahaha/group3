import requests
import unittest
from selenium import webdriver
from time import sleep
from FrameDemo.SharedParkingPlace.Tool.api_util import APIUtil

class TestUnitTest_Api_Cases(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_weather_changsha(self):
        drive = self.driver
        data = APIUtil.api_data()
        for case in data:
            print('正在执行第{}条用例'.format(case['caseid']))
            resul = APIUtil.request(case['remethod'], case['uri'], case['params'])  # 获得请求的响应结果
            result = resul.text
            i = 0
            while i>40:
                self.assertEqual(result,case['expect'])
                i +=1



if __name__ == '__main__':
    unittest.main()