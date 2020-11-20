import requests
from FrameDemo.SharedParkingPlace.Tool.api_util import APIUtil
from FrameDemo.SharedParkingPlace.Tool.file_uite import File_Uite
from FrameDemo.SharedParkingPlace.Test.test_report import TestReport


class requests_sell:
    def __init__(self):
        self.domain_url = "http://192.168.1.103:8888/WoniuSales1.4"

        self.session = requests.Session()  # 实例化一个Session对象

    def api_login(self):

        self.login_uri = "/user/login"
        custom_header = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
        login_data = "username=admin&password=Milor123&verifycode=0000"

        res = requests.request(
            method="POST",
            url=self.domain_url +
            self.login_uri,
            data=login_data,
            headers=custom_header)
        print(res.text)

        if res.text == "login-pass":
            print("登录接口测试通过")
        else:
            print("登录接口测试失败")
        return res.cookies

    def api_sell(self):  # 获取session获取Cookie登录后进行下一步
        api_sell_info = File_Uite().get_ini_section(
            '../Test_data/interfacedata_sell.ini', 'api_request')
        APIUtil().request(
            api_sell_info['port'],
            api_sell_info['url'],
            api_sell_info['data'])
        APIUtil().assert_api(api_sell_info[['data']])

    def sell_pohone(self):
        api_sell_pohone = File_Uite().get_ini_section(
            '../Test_data/interfacedata_sell.ini', 'pohone_request')
        APIUtil().request(
            api_sell_pohone['port'],
            api_sell_pohone['url'],
            api_sell_pohone['data'])
        APIUtil().assert_api(api_sell_pohone[['data']])

    def sell_confirm(self):
        api_sell_confirm = File_Uite().get_ini_section(
            '../Test_data/interfacedata_sell.ini', 'confirm_request')
        APIUtil().request(
            api_sell_confirm['port'],
            api_sell_confirm['url'],
            api_sell_confirm['data'])
        APIUtil().assert_api(api_sell_confirm[['data']])

    def write_report(self):
        result = File_Uite.get_txt(
            '../Test_data/result/result.txt')  # 根据结果生成报告
        result_list = []
        error_msg_list = []
        sceenshot_list = []
        if result in '页面存在该元素，测试成功':
            result_list.append('测试通过')
        else:
            result_list.append('测试不通过')

        list1 = File_Uite().read_excel_value("../Test_data/test_info.ini", 'login')

        result_info = [
            list1[0]['version'],
            list1[0]['module'],
            list1[0]['type'],
            list1[0]['caseid'],
            list1[0]['desc'],
            result_list,
            error_msg_list,
            sceenshot_list,
            list1[0]['uri'],
            list1[0]['remethod'],
            list1[0]['username'] +
            list1[0]['password'] +
            list1[0]['verifycode'],
            list1[0]['expect'],
        ]
        TestReport("report_db").write_report_db(result_info)
        TestReport('report_db').generate_html_report('v2.0')


if __name__ == '__main__':
    temp = requests_sell()
    temp.api_login()
    temp.api_sell()
    temp.sell_pohone()
    temp.sell_confirm()
