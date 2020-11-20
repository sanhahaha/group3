import requests
import os

from FrameDemo.SharedParkingPlace.Tool.file_uite import File_Uite


class APIUtil:
    def __init__(self):
        self.domain_url = "http://172.16.13.181:8080/SharedParkingPlace/"
        self.session = requests.Session()  # 实例化一个Session对象

    def get_session(self):
        '''
        读取url,data文件
        获取具有Cookie的session
        此项目需要登录页面的session和登录的session
        :return:
        '''
        uri = File_Uite().read_excel_value("../Test_data/test_info.ini", 'api_share')[0]['uri']
        data = File_Uite().read_excel_value("../Test_data/test_info.ini", 'api_share')[0]['params']

        self.session.get('http://172.16.13.181:8080/SharedParkingPlace/image') # 登录页面的session
        res = self.session.get(uri+data)
        print("获取的session结果：",res.text)
        return self.session

    @classmethod
    def request(cls,method,url,data=None):
        '''
        发送请求获得响应
        :param method: 请求方式
        :param url: 请求url
        :param data: 请求数据
        :return: 响应结果
        '''
        session = APIUtil().get_session()
        resp = getattr(session,method)(url,params = data)
        return resp

    @classmethod
    def assert_api(cls, test_info):
        resp = APIUtil.request(test_info['request_method'], test_info['uri'], test_info['params'])
        print(resp)
        from FrameDemo.SharedParkingPlace.Tool.image_identification import Assert
        Assert.assert_equal(resp, resp)

    @classmethod
    def api_data(cls):

        '''
        测试数据
        'caseid'  'module' 'type' 'uri' 'remethod' 'desc' 'params' 'expect'
        '''
        test_case = File_Uite().read_excel_value("../Test_data/test_info.ini", 'api_share')
        return test_case

    @classmethod
    def api_start(cls):
        # 调用函数,发起请求
        data = cls.api_data()
        for case in data:
            print('正在执行第{}条用例'.format(case['caseid']))
            resul = cls.request(case['remethod'], case['uri'], case['params'])  # 获得请求的响应结果
            result = resul.text
            if case['expect'] == result:
                print('第{}条用例：{}——测试通过'.format(case['caseid'], case['desc']))
            else:
                print('第{}条用例：{}——测试失败'.format(case['caseid'], case['desc']))



if __name__ == '__main__':

    api = APIUtil()
    # print(api.api_data())
    api.api_start()