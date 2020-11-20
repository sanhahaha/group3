from pycharm.测试框架.woniutestV1.action.login_ui import Login
from pycharm.测试框架.woniutestV1.tools.lib_util import FileUtil,UiUtil
from pycharm.测试框架.woniutestV1.action.sales_conditon_search_ui import sales_search

class Test_sales_search:
    def __init__(self,driver):
        self.driver = driver #以后编程driver都从代码执行区传入；



    def recycle_test_sales(self,path,section,option): #参数要使用在打开excel文件相关
        contents = FileUtil.get_test_info(path,section,option)
        print(contents)
        #待取出整个数据之后，循环使用这些数据进行查询操作；当然也可以把登录放在init方法里面，每进行一次登录，可以进行多次测试查询；
        print("****************************")
        i=0
        for content in contents:
            search_data = content["params"] #只取了使用的参数数据；其他的后续使用的时候，根据键名再取；
            print(search_data)
            #开始调用 查询功能；是不需要注销的；任何界面都是可以点击库存查询的；点击了查询以后，再次输入就行，封装好的方法里面有，点击后，清除内容的功能；

            #调用测试 查询的方法；
            sales_search(driver).do_search(search_data)
            i = i+1
            print(f"第{i}次测试销售出库按条件查询功能")

            #暂时没有写入断言的方法；
            ##################
            ##################
            ##################




if __name__ == '__main__':
    driver = UiUtil.get_driver()
    # 只登录一次，后面每次测试都是在这一次登录的基础上进行，不需要重复注销再进入进行测试
    # 填写的数据，在调用input方法的时候，会被清除clear,所以不会影响；
    login_data = {'username': 'admin', 'password': 'Milor123', 'verifycode': '0000'}
    Login(driver).do_login(login_data)


    Test_sales_search(driver).recycle_test_sales("..\\conf\\test_info.ini","sales","query_conditon_ui")
