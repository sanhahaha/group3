from FrameDemo.SharedParkingPlace.Tool.gui_util import uiutil
from FrameDemo.SharedParkingPlace.Tool.file_uite import File_Uite
from FrameDemo.SharedParkingPlace.Tool.file_uite import logutil
from FrameDemo.wntest.action import login
import os
class Customer:
    phone = "customerphone"
    name = "customername"
    sex = "#childsex"
    sexs = ('# childsex > option:nth-child(2)')
    child = "childdate"
    credit = "creditkids"
    clothin = "creditcloth"
    buttnew = ("/html/body/div[4]/div[1]/form[2]/div[2]/button[1]")
    buttalt = "editBtn"
    buttque = ("/html/body/div[4]/div[1]/form[2]/div[2]/button[3]")
    prepa = ("/html/body/div[4]/div[2]/table/tbody/tr[2]/td/a[1]")
    nepa = ("/html/body/div[4]/div[2]/table/tbody/tr[2]/td/a[2]")
    bua = ("/html/body/div[4]/div[2]/table/tbody/tr[1]/td[11]/a")
    births = '#childdate'
    births1 = '.datetimepicker-days > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(4) > td:nth-child(7)'
    def __init__(self):
        self.driver = uiutil.get_driver()
        self.driver.implicitly_wait(5)
        self.data = File_Uite.get_ini_section('..\\Test_data\\test_info.ini', 'login')

    def number(self, numbers):  # 手机号码 1
        uiutil().input((self.driver.find_element_by_id(self.phone)),numbers)

    def members_nickname(self, nickname):  # 会员昵称 2
        uiutil().input((self.driver.find_element_by_id(self.name)),nickname)


    def baby_gender(self):  # 小孩性别 3
        uiutil().click(self.driver.find_element_by_css_selector(self.sex))


    def birth(self):  # 日期 4
        uiutil().click(self.driver.find_element_by_css_selector(self.births))
        uiutil().click(self.driver.find_element_by_css_selector(self.births1))


    def child_integral(self, integral):  # 母婴积分 5
        uiutil().input((self.driver.find_element_by_id(self.credit)),integral)

    def clothing_integral(self, clothing):  # 童装积分 6
        uiutil().input((self.driver.find_element_by_id(self.clothin)),clothing)


    def button_newappend(self):  # 新增按钮 11
        uiutil().click(self.driver.find_element_by_xpath(self.buttnew))

    def button_alter(self):  # 修改按钮 22
        uiutil().click(self.driver.find_element_by_id(self.buttalt))

    def button_query(self):  # 查询按钮 33
        uiutil().click(self.driver.find_element_by_xpath(self.buttque))

    def main_alter(self): # 修改按钮 修改
        uiutil().click(self.driver.find_element_by_xpath(self.bua))

    def main_pageup(self): # 修改按钮 上一页
        uiutil().click(self.driver.find_element_by_xpath(self.prepa))

    def main_pagedown(self): # 修改按钮 下一页
        uiutil().click(self.driver.find_element_by_xpath(self.nepa))

    def into_customer_page(self):
        username = self.data[0]['username']
        password = self.data[0]['password']
        verifycode = self.data[0]['verifycode']
        login.Login(
            self.driver).do_login(
            username,
            password,
            verifycode)
        uiutil().click(self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/ul[1]/li[5]/a"))

    def add_into(self,numbers, nickname, integral, clothing):
        self.number(numbers)
        self.members_nickname(nickname)
        self.baby_gender()
        self.birth()
        self.child_integral(integral)
        self.clothing_integral(clothing)
        self.button_newappend()

    def query_into(self,numbers):
        self.number(numbers)
        self.button_query()

    def alter_into(self,numbers,number_to):
        self.number(numbers)
        self.button_query()
        self.main_alter()
        self.number(number_to)
        self.button_alter()



if __name__ == '__main__':
    obj = Customer()
    obj.into_customer_page()
    obj.birth()
    obj.baby_gender()