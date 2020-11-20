# 注释：
# 根据action里面写好的登录login方法；本次调用时候，传入从excel中读取的数据，
# 因为excel是多组数据，所以需要使用for循环，进行登录操作；根据excel的长度，确定登录循环的次数；
# 注意从从第二次登录开始，需要每次点击一下注销按钮；可以把该方法添加到inspector.ini文件中去；

#  用作模板，待修改；


import time

from selenium.webdriver.common.by import By

from woniutestV1.action.login_ui import Login
from woniutestV1.tools.lib_util import UiUtil
from woniutestV1.tools.util import FileUtil

class TestLogin:
    def __init__(self,driver):
        self.driver = driver

    def do_login_test(self,path,section,option): #根据路径打开的文件含有excel的地址信息，根据这个地址，再去打开excel文件、
        contents = FileUtil.get_test_info(path,section,option)#三个参数，分别是含含有excel相关数据的存放地址，section和option值
        # print(contents)
        i= 0
        for content in contents:
            i=i+1
            # 执行登录操作；
            Login(self.driver).do_login(content)
            #使用try抛出异常，去定位元素；
            try:
                logout_button_element = UiUtil.find_elment("login",'logout_button')
                UiUtil.click(logout_button_element)
                print(f"第{i}次 登录成功")

            except:
                time.sleep(2)
                print(f"第{i}次 登录失败")
                self.driver.refresh()



if __name__ == '__main__':
    driver = UiUtil.get_driver()
    TestLogin(driver).do_login_test('..\\conf\\test_info.ini','login','login_info')
    #根据section和option取到了excel相关的信息，返回值是一个大列表，里面的每组数据是一个字典；
