if __name__ == '__main__ ':
    import requests
    test_data = [({"mobileNumber":"13021671512"},
                  {'expect' : { "error_code" :0,
                            "reason": "Succes",
                            "result": {
                                "mobilenumber": "1302167",
                                "mobilearea": "山东 青岛市",
                                "mobiletype":"联通如意通卡",
                                "areacode" : "0532",
                                "postcode": "266000"}
                             }
                }),
                 ({"mobileNumber": ""}, {' expect ' : { "error _code" : 1,
                            "reason": "Fail",
                            "result": {
                                }
                            }}),
                ({"mobileNumber": "123"}, {'expect ': {"error_code": 1,
                            "reason": "Fail",
                            "result": {
                                }
                            }})]
    url = 'http://api.avatardata.cn/MobilePlace/LookUp'
    for data in test_data :
        param = data[0]  #拿到第一段（每个元组）第一句
        resp = requests.post(url, param)
        acutal = resp.json()#字符串转json   返回响应码
        if acutal == data[1]['expect']:
            print('test pass')
        else:
            print('test fail')




