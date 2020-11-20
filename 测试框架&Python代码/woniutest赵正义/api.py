import requests

# 接口地址：http: // api.avatardata.cn / MobilePlace / LookUp
# 返回格式：JSON
# 请求方式：POST
# 接口备注：通过手机号码查询归属地城市，以及手机卡信息，区号和邮编
# 请求参数：
# 名称
# 类型
# 必填
# 说明
# mobileNumber
# String
# 是
# 手机号码
# 错误码参照：
# 错误码
# 说明
# 0
# 请求成功
# 1
# 参数错误
# 例子：mobileNumber = 13021671512, JSON返回结果如下
# {
#
#     "error_code": 0,
#
#     "reason": "Succes",
#
#     "result": {
#
#         "mobilenumber": "1302167",
#
#         "mobilearea": "山东 青岛市",
#
#         "mobiletype": "联通如意通卡",
#
#         "areacode": "0532",
#
#         "postcode": "266000"
#
#     }
#
# }
#
# 请用python的requests库对这个接口进行测试
import requests
import json5

def session_login():

    phone_url = "http://api.avatardata.cn/MobilePlace/LookUp" ##url
    phone_data = {"mobilenumber": "13021671512"}  ##上传参数
    header = {"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}  ##请求的content——type
    res = requests.request(method="POST", url=phone_url,data= phone_data, headers=header)
    respond_code = res.status_code
    result = json5.loads(res.text)
    print(type(res.json()))

    print(respond_code)
    print(type(res.text))

if __name__ == '__main__':
    session_login()