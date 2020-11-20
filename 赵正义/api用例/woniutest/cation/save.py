from woniutest.cation.logintest import Login
from woniutest.ui_util.web_ui import UiUtil


class  Save:
    def __init__(self):
        driver = UiUtil.get_driver()
        Login(driver).do_login({"username": "admin", "password": "admin123", "verifycode": "0000"})
    def input_hao(self,hao):
        element = UiUtil.find_elment('save', 'hao')
        UiUtil.input(element, hao)
    def input_name(self,name):
        element = UiUtil.find_elment('save', 'name')
        UiUtil.input(element,name)
        pass
    def input_barcode(self,name):
        element = UiUtil.find_elment('save', 'bar')
        UiUtil.input(element, name)
        pass
    def click_save(self):
        element = UiUtil.find_elment('save', 'text')
        UiUtil.click(element)
        pass
    def riqiz(self,zao,id):
        element = UiUtil.find_elment('save', 'zao')
        # js = "$('input[id=earlystoretime]').attr('readonly','')"
        UiUtil.alter_seletor_input(element, zao,id)
    def riqiwan(self,wan,id):
        element = UiUtil.find_elment('save', 'wan',)
        # js = "$('input[id=laststoretime]').attr('readonly','')"
        UiUtil.alter_seletor_input(element,wan,id)
    def type(self,t):
        element = UiUtil.find_elment('save', 'type')
        UiUtil.select_text(element,t)
    def click_type(self):
        element = UiUtil.find_elment('save', 'type_click')
        UiUtil.click(element)
    def do(self,date):
            self.click_save()
            self.input_name(date["name"])
            self.input_barcode(date["bar"])
            self.input_hao(date["hao"])
            self.type(date["t"])
            self.riqiwan(date["wan"],date["wid"])
            self.riqiz(date["zao"],date["zid"])
            self.click_type()



if __name__ == '__main__':
    pass
    a=Save()
    a.do({"name":"米乐果后开连衣裙","bar":"11111111","hao":"M3Q1498B","wan":"2020-11-07",
          "zao":"2013-04-01","wid":"laststoretime","zid":"earlystoretime","t":"衣服"})