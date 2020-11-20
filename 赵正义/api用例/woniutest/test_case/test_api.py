import unittest

from woniutest.ui_util.web_ui import Api
from woniutest.tool.util import FileUtil
from  parameterized import parameterized

# class TestSalesAPI(unittest.TestCase):
#
#     def test_scan_barcode(self):
#
#         test_info = FileUtil.get_excel_api('..\\conf\\test_info.ini', 'login', 'login_info_api')
#         print(test_info)
#         Api.assert_api(test_info)
#
#     def query_customer(self):
#         test_info = FileUtil.get_excel_api('..\\conf\\test_info.ini', 'login', 'login_info_api')
#         Api.assert_api(test_info)
class Caradd(unittest.TestCase):
    def setUp(self):
        pass

    def test_1caradd(self):
        test_info = FileUtil.get_excel_api('..\\conf\\test_info.ini', 'car', 'caradd')
        Api.assert_api(test_info)
    def test_2changeuser(self):
        test_info = FileUtil.get_excel_api('..\\conf\\test_info.ini', 'car', 'changeuser')
        Api.assert_api(test_info)

    def test_3delete(self):
        test_info = FileUtil.get_excel_api('..\\conf\\test_info.ini', 'car', 'delete')
        Api.assert_api(test_info)
    def test_4comments(self):
        test_info = FileUtil.get_excel_api('..\\conf\\test_info.ini', 'car', 'comments')
        Api.assert_api(test_info)

    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()
