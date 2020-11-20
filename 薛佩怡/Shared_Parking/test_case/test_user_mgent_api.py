from Shared_Parking.tools.lib_util import APIUtil,Assert
from Shared_Parking.tools.util import FileUtil


class TestUserMgentAPI:

    # # 试验版：直接使用封装的request方法去看响应结果，响应结果正确
    # def test_query_api(self):
    #
    #     request = APIUtil.request('get',
    #                               'http://192.168.226.146:8080/SharedParkingPlace/admin/tenant/peopertyFindTenants/',
    #                               {'uname': '周友', 'page': '1', 'rows': '10'} )
    #     print(request.text)


    def test_query_api(self):
        # 使用get_test_info方法读取ini文件（里面有Excel路径）中的excel相关数据
        # get_test_info方法中还有get_ini_value读取方法
        test_info = FileUtil.get_test_info('..\\conf\\test_info.ini','user_mgent','query_api')

        # 遍历test_info（列表套字典，根据字典的键取出来值，这些值是request方法的参数）
        # request.text将打印出接口的响应信息
        for data in test_info:
            request = APIUtil.request(data["request_method"],data["uri"],data["params"])
            APIUtil.assert_api(test_info)



if __name__ == '__main__':
    TestUserMgentAPI().test_query_api()







