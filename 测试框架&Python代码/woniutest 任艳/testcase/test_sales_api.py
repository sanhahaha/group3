from pycharm.测试框架.woniutestV1.tools.lib_util import APIUtil, Assert
from pycharm.测试框架.woniutestV1.tools.util import FileUtil


class TestSalesAPI:

    def test_scan_barcode(self):

        test_info = FileUtil.get_test_info('..\\conf\\test_info.ini', 'sales', 'scan_barcode_api')
        APIUtil.assert_api(test_info)

    def query_customer(self):
        test_info = FileUtil.get_test_info('..\\conf\\test_info.ini', 'sales', 'query_customer_api')
        APIUtil.assert_api(test_info)



if __name__ == '__main__':
    TestSalesAPI().test_scan_barcode()