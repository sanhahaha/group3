


from pycharm.测试框架.woniutestV1.tools.lib_util import APIUtil, Assert
from pycharm.测试框架.woniutestV1.tools.util import FileUtil

class TestRobAPI:

    def test_scan_barcode(self):
        test_info = FileUtil.get_test_info('..\\conf\\test_info.ini', 'customer', 'rob_login_api')
        APIUtil.assert_api(test_info)


if __name__ == '__main__':
    TestRobAPI().test_scan_barcode()