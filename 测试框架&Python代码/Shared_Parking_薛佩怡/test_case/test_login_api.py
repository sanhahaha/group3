import unittest

from Shared_Parking.tools.lib_util import APIUtil,Assert
from Shared_Parking.tools.util import FileUtil


class TestLoginAPI(unittest.TestCase):


    def test_login(self):
        test_info = FileUtil.get_test_info('..\\conf\\test_info.ini','login','login_api')
        APIUtil.assert_api(test_info)

        # 从conf层的test_info.ini文件中读取login模块的login_api相关数据
        # login_api数据在Excel表中
        # get_text_info方法是读取Excel的相关信息



if __name__ == '__main__':
    TestLoginAPI().test_login()



   # # 以下为调试代码
   #  import requests
   #  res = requests.get('http://192.168.226.146:8080/SharedParkingPlace/login',
   #                     {'uname':'物业0','upass':'123','imgcode':'0000'})
   #  print(res.text)