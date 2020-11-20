
from pycharm.测试框架.woniutestV1.tools.lib_util import APIUtil, Assert
from pycharm.测试框架.woniutestV1.tools.util import FileUtil


class TestCustomer:

    def test_add_customer(self):
        test_info = FileUtil.get_test_info('..\\conf\\test_info.ini', 'rob', 'rob_case_api')
        APIUtil.assert_api(test_info)


if __name__ == '__main__':
    #测试新增功能
    TestCustomer().test_add_customer()