from FrameDemo.SharedParkingPlace.Tool.gui_util import uiutil
from FrameDemo.SharedParkingPlace.Action.do_login import login


class Dosales:

    def __init__(self,driver):
        self.driver = driver

    def input_barcode(self, barcode):
        bcode = self.driver.find_element_by_id('barcode')
        uiutil.input(bcode, barcode)


    def click_barcode_button(self):
        uiutil.click(self.driver.find_element_by_xpath('//form[@class="form-inline"]/button'))


    def input_phone(self, customerphone):
        cphone = self.driver.find_element_by_id('customerphone')
        uiutil.input(cphone, customerphone)


    def click_cphone_button(self):
        uiutil.click(self.driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[1]/form/div[2]/button'))


    def click_submit(self):
        uiutil.click(self.driver.find_element_by_id('submit'))


    def confirm_alert(self):
        self.driver.switch_to.alert.accept()

    def start_login(self):
        login(self.driver).do_login('admin', 'Milor123', '0000')

    def start_sales(self):
        self.input_barcode(11111111)
        self.click_barcode_button()
        self.input_phone(186836668866)
        self.click_cphone_button()
        self.click_submit()
        self.confirm_alert()
        self.driver.close()

if __name__ == '__main__':
    obj = Dosales(uiutil.get_driver())
    obj.start_login()
    obj.start_sales()