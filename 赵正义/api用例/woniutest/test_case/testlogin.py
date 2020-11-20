import time
from woniutest.cation.add_vip import vip
from woniutest.cation.login import Login
from woniutest.tool.util import FileUtil
from woniutest.ui_util.web_ui import UiUtil


class Log:
    def __init__(self):
        self.driver=UiUtil.get_driver()
    def login(self):
        data=FileUtil.get_excel('..\\conf\\test_info.ini', 'login', 'login_info')
        print(data)
        for i in range(len(data)):
            Login(self.driver).do_login(data[i])
            a=self.driver.find_element_by_xpath(
                '//*[@id="navbar"]/ul[2]/li[1]/a').text
            if data[i]["expect"] ==  "login-sucess":
                print(data[i]["expect"])
                print(data[i]["username"])
                if data[i]["username"] in a:
                    print("成功")
                    print(data[i]["username"])
                    Login(self.driver).logout()
                elif  a != "尚未登录":
                    print("失败")
                    Login(self.driver).ok()
                    time.sleep(1)
            else:
                if data[i]["username"] in a and a != "尚未登录":
                    print(data[i]["username"])
                    print(a)
                    print("失败")
                    Login(self.driver).logout()
                else:
                    print("成功")
                    print(data[i]["username"])
                    Login(self.driver).ok()
                    time.sleep(1)
            # except:




    # def vip1(self):
    #     self.login()
    #     data = FileUtil.get_excel("../conf/woniu.json", 1)
    #     vip(self.driver).do_vip()


if __name__ == '__main__':
    Log().login()