from woniutest.tool.util import FileUtil
from woniutest.ui_util.web_ui import UiUtil


class vip:
    def __init__(self, driver):
        self.driver = driver

    def click_vip(self):
        ele = self.driver.find_element_by_link_text("会员管理")
        UiUtil.click(ele)

    def input_phone(self,phone):
        ele = self.driver.find_element_by_id("customerphone")
        UiUtil.input(ele, phone)

    def input_name(self,name):
        ele = self.driver.find_element_by_id("customername")
        UiUtil.input(ele,name)

    def input_sex(self):
        ele = self.driver.find_element_by_id("childsex")
        UiUtil.select_or(ele)

    def riqi(self,ripi):
        ele = self.driver.find_element_by_id("childdate")
        UiUtil.alter_seletor_input(ele, ripi)

    def add_vip_click(self):
        ele = self.driver.find_element_by_xpath(
            "/html/body/div[4]/div[1]/form[2]/div[2]/button[1]")
        UiUtil.click(ele)

    def vip_query(self):
        ele = self.driver.find_element_by_xpath(
            "/html/body/div[4]/div[1]/form[2]/div[2]/button[1]")
        UiUtil.click(ele)
    def do_vip(self,phone,name,riqi):
        self.click_vip()
        self.input_phone(phone)
        self.input_name(name)
        self.input_sex()
        self.riqi(riqi)
        self.add_vip_click()
