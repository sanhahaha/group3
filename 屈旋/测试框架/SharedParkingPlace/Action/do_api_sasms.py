from FrameDemo.SharedParkingPlace.Tool.file_uite import File_Uite
from FrameDemo.SharedParkingPlace.Tool.api_util import APIUtil
import time

class SasmsAPI:

    def __init__(self):
        pass


    def sasms_param(self):
        value = File_Uite().read_excel_value("../Test_data/test_info.ini", 'api_share')

        # APIUtil().request()
        methodl = [] # 请求方法
        uril = [] # 请求链接
        datal = [] # 请求参数
        for i in range(len(value)):
            val = i+1,value[i]
            method = val[1]["remethod"]
            uri = val[1]["uri"]
            data = val[1]["params"]
            methodl.append(method)
            uril.append(uri)
            datal.append(data)
        return methodl,uril,datal


    def start_sasms(self):
        '''
        一次尝试
        x,y,z组数据,依次按照x[0],y[0]...x[1],y[1]顺序去取值，并添加到方法中对应参数位置的数据执行
        最高依次执行三个
        :return:
        '''
        obj = self.sasms_param()
        methods = obj[0]
        uris = obj[1]
        paramss = obj[2]
        print(methods, '\n', uris, '\n', paramss)
        method = methods[0:3]
        uri = uris[0:3]
        params = paramss[0:3]
        # 会出现问题，too many values to unpack (expected 3) 还是依照用例一条
        method_index = 0
        uri_index = 0
        obj_index = 0
        for i, j, k in method, uri, params:
            method1 = method[method_index]
            uri1 = uri[uri_index]
            params1 = params[obj_index]
            method_index += 1
            uri_index += 1
            obj_index += 1

            if APIUtil():
                APIUtil().request(method1, uri1, params1)
                time.sleep(0.1)





if __name__ == '__main__':
    obj = SasmsAPI()
    obj.start_sasms()