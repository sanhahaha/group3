# 新增会员的接口测试；

from pycharm.测试框架.woniutestV1.tools.lib_util import APIUtil,Assert
from pycharm.测试框架.woniutestV1.tools.util import FileUtil


class TestCustomer:

    def test_query_customer(self):
        test_info = FileUtil.get_test_info('..\\conf\\test_info.ini', 'customer', 'query_customer_api')
        APIUtil.assert_api(test_info)


if __name__ == '__main__':
    # 测试查询功能
    TestCustomer().test_query_customer()