# 同级别的主界面展示未封装；
# 使用映射的操作，将find_element的操作的参数，放在 inspector里面；
from woniutestV1.action.login_ui import Login
from woniutestV1.tools.lib_util import UiUtil

class sales_search:
    def __init__(self,driver):
        self.driver = driver


        # 登录可以写入初始值方法，也可以放下下面执行输入的各种操作汇总里面；
        # 调用登录的方法，作为前置条件，登陆后才有的
        # 不然每次执行测试方法，都需要去重新登录一次，
    #进入库存查询界面
    def click_store_page(self):
        store_page_element = UiUtil.find_elment("sales","store_page")
        UiUtil.click(store_page_element)

    #输入货号
    def input_goodsserial(self,serial):
        goods_serial_element= UiUtil.find_elment("sales","goods_serial") #等写了框架，把信息写入inspector文件；
        UiUtil.input(goods_serial_element,serial)

    #输入品名
    def input_goodsname(self,name):
        goods_name_element = UiUtil.find_elment("sales", "goods_name")
        UiUtil.input(goods_name_element,name)

     #输入条形码；
    def input_barcode(self,barcode):
        barcode_element = UiUtil.find_elment("sales",'barcode')
        UiUtil.input(barcode_element,barcode)

    #输入类别；
    def input_goodstype(self,type):
        serial_element = UiUtil.find_elment("sales",'goods_type')
        #下拉框,只需要输入两个参数即可；
        UiUtil.select_by_text(serial_element,type)


    # 最早入库时间；需要调用一个封装好，修改时间设置的函数；
    def input_early_storetime(self,earlytime):
        early_storetime_element = UiUtil.find_elment("sales",'early_time')

        js = 'document.getElementById("earlystoretime").removeAttribute("readonly")'
        self.driver.execute_script(js)

        UiUtil.input(early_storetime_element,earlytime)

    # 最迟入库时间；
    def input_last_storetime(self,lasttime):
        last_storetime_element = UiUtil.find_elment("sales","last_time")
        # 待封装；
        js = 'document.getElementById("laststoretime").removeAttribute("readonly")'
        self.driver.execute_script(js)
        # 待封装；
        UiUtil.input(last_storetime_element, lasttime)

    # 点击搜索按钮；
    def click_search_button(self):
        search_button_element=UiUtil.find_elment("sales","search_button")
        UiUtil.click(search_button_element)


    # 上面的各个操作，整合为一个完整的 按条件搜索测试过程

    def do_search(self,serch_data):


        #点击进入禄存查询
        self.click_store_page()
        self.input_goodsserial(serch_data['serial'])
        self.input_goodsname(serch_data['name'])
        self.input_barcode(serch_data['barcode'])#键名之后要和excel文件中的键名相对应；
        self.input_goodstype(serch_data['type'])
        self.input_early_storetime(serch_data['earlytime'])
        self.input_last_storetime(serch_data['lasttime'])
        self.click_search_button()




if __name__ == '__main__':
    driver = UiUtil.get_driver()
    # 调用登录的方法
    login_data = {'username': 'admin', 'password': 'Milor123', 'verifycode': '0000'}
    Login(driver).do_login(login_data)

    serch_data = {"serial": "M1Q0648B", "name": "冰蓝纯棉背心裙", "barcode": "22222222", "type": "衣服",
                  "earlytime": "2018-05-03", "lasttime": "2018-05-11"}
    # 调用方法，必须有，传入参数；
    mytest = sales_search(driver).do_search(serch_data)









