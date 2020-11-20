from FrameDemo.SharedParkingPlace.Tool.gui_util import uiutil
from FrameDemo.SharedParkingPlace.Action.do_login import login
from selenium import webdriver

class Dostore:
    def __init__(self):
        self.driver = uiutil.get_driver()
        self.driver.implicitly_wait(5)


    def click_store(self):
        uiutil().click(self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/ul[1]/li[4]/a'))

    def input_art(self):
        uiutil().input(self.driver.find_element_by_id('goodsserial'), 'M3Q1498B')


    def click_condtion_query(self):
        uiutil().click(self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/form[2]/div[2]/input[3]'))


