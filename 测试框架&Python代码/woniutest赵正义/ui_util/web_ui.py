import random
import time
from selenium.webdriver.common.by import By
import cv2
from PIL import ImageGrab
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
from woniutest.tool.util import LogUtil, TimeUtil
import os
from woniutest.tool.util import FileUtil
from selenium import webdriver
from pymouse import PyMouse
from pykeyboard import PyKeyboard
# webdriver.Chrome
class Api:
    @classmethod
    def get_session(cls):
        import requests
        session = requests.session()
        c=session.get(url="http://192.168.186.159:8080/SharedParkingPlace/image")
        login_url = FileUtil.get_ini("../conf/base.ini","api","login_url")
        res=session.get(url=login_url)
        # print(res.text)
        return session
    @classmethod
    def request(cls,method,url,data = None):

        session=cls.get_session()
        resp = getattr(session,method)(url,params = data)
        # print(resp.text)
        return resp
    @classmethod
    def  assert_api(cls,test_info):
        # print(test_info)

        for info in test_info:
            resp = Api.request(info["request_method"],info["uri"],info["params"])
            print(info["expect"])
            print(resp.text)
            print(info["desc"])
            UiUtil.assert_equal_api(resp.text,info["expect"])
            print("################################################################")


        # # print(test_info)
        #
        # resp = Api.request(test_info["request_method"],test_info["uri"],test_info["params"])
        # print(test_info["expect"])
        # print(resp.text)
        # # return  test_info["expect"],resp.text





    # @classmethod
    # def get_resp(cls,test_info):
    #     return cls.request(test_info["request_method"],test_info["uri"],test_info["params"])
    #
    # @classmethod
    # def do_request(cls,info):
    #     li = []
    #     for test_info in info:
    #         resp = Api.get_resp(test_info)
    #         li.append(resp)
    #     return li





class UiUtil:
    mmm="000"
    mouse = PyMouse()
    keyboard = PyKeyboard()
    driver = None
    logger = LogUtil.get_logger(os.path.join(os.getcwd(), "web_ui"))

    @classmethod  # 'login', 'uname'
    def find_elment(cls, section, option):

        attr =0
        try:
            element_attr = FileUtil.get_ini_list('..\\conf\\base.ini', section)

            for element in element_attr:
                if option in element.keys():
                    attr = eval(element[option])
            return cls.driver.find_element(getattr(By, attr[0]), attr[1])
        except:
            return None

    @classmethod
    def get_driver(cls):
        from selenium import webdriver
        try:
            browser = FileUtil.get_ini("../conf/base.ini", "ui", "browser")
            url = FileUtil.get_ini("../conf/base.ini", "ui", "url")
            print(browser)
            if cls.driver is None:
                cls.driver = getattr(webdriver, browser)()
                cls.driver.maximize_window()
                cls.driver.get(url)
                cls.driver.implicitly_wait(5)
        except BaseException:
            cls.logger.error("driver生成失败请检查配置文件中的浏览器名字")
        return cls.driver
    @classmethod
    def queding(cls):  # 删除
        cls.driver.switch_to.alert.accept()  # 确定
    @classmethod
    def quxiao(cls):  # 内容
        cls.driver.switch_to.default_content()

    @classmethod
    def input(cls, element, text):
        element.click()
        element.clear()
        element.send_keys(text)

    @classmethod
    def click(cls, element):
        print(element)
        element.click()

    @classmethod
    def select_or(cls, element):
        """
        任意的    下拉框选值
        :param element:
        :return:
        """
        random_index = random.randint(0, len(Select(element).options) - 1)
        Select(element).select_by_index(random_index)

    @classmethod
    def select_text(cls, element, text):
        '''

        :param element:
        :param text:
        :return:
        '''
        Select(element).select_by_visible_text(text)

    @classmethod
    def DOWN(cls, element):
        """
        滚动条滚到某个位置（元素）
        :param element:
        :return:
        """

        element.send_keys(Keys.DOWN)

    @classmethod
    def alter_seletor_input(cls, element, value  ,id):
        """
        将选择日期框修改为可直接输入
        :param element: 操作元素
        :param value:
        :return:
        """
        js = f'document.getElementById("{id}").removeAttribute("readonly")'
        cls.driver.execute_script(js)
        # js = "$('input[id=%s]').attr('readonly','')" %id # 设置为空
        # cls.driver.execute_script(js)  # 执行设置为空
        element.send_keys(value)

    @classmethod
    def find_image(cls, target):
        image_path = "../image"
        screen_path = os.path.join(image_path, 'screen.png')
        ImageGrab.grab().save(screen_path)
        # 读取大图对象
        screen = cv2.imread(screen_path)
        # 读取小图对象
        template = cv2.imread(os.path.join(image_path, target))
        # 进行模板匹配，参数包括大图对象、小图对象和匹配算法
        result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        # 获取匹配结果
        min, max, min_loc, max_loc = cv2.minMaxLoc(result)
        similarity = FileUtil.get_ini("../conf/base.ini", "ui", "similarity")
        if max < float(similarity):
            return -1, -1
        x = max_loc[0] + int(template.shape[1] / 2)
        y = max_loc[1] + int(template.shape[0] / 2)
        return x, y

    @classmethod
    def click_image(cls, target):
        x, y = cls.find_image(target)
        if x == -1 and y == -1:
            cls.logger.error(f"{target}未匹配")
            return
        cls.mouse.click(x, y)

    @classmethod
    def double_click_image(cls, target):
        x, y = cls.find_image(target)
        if x == -1 and y == -1:
            cls.logger.error(f"{target}未匹配")
            return
        cls.mouse.click(x, y, n=2)

    @classmethod
    def input_image(cls, target, msg):
        x, y = cls.find_image(target)
        if x == -1 and y == -1:
            cls.logger.error(f"{target}未匹配")
            return



        print(x,y)
        time.sleep(0.2)
        cls.mouse.click(x, y)
        time.sleep(0.1)
        cls.keyboard.type_string(msg)
        # time.sleep(0.1)
        # cls.enter()

        time.sleep(0.5)
        cls.keyboard.press_key(" ")

    @classmethod
    def select_image(cls, target, count):
        cls.click_image(target)
        for i in range(count):
            cls.keyboard.press_key(cls.keyboard.down_key)
        cls.keyboard.press_key(cls.keyboard.enter_key)

    @classmethod
    def enter(cls):
        cls.keyboard.press_key(cls.keyboard.enter_key)

    @classmethod
    def is_element_present(cls, driver, how, what):
        """
        该方法用于判断某个元素是否存在
        :return:
        """
        try:
            print(how, what)
            driver.find_element(how, what)
            return True
        except:
            cls.logger.error(f'没有找到方式为{how}值为{what}的元素')
            return False

    @classmethod
    def assert_equal(cls, driver, expect, actual):
        if expect == actual:
            return True
        else:
            # ..\\screenshot\\LogUtil.get_ctime()_error.png
            driver.get_screenshot_as_file(f'..\\screenshot\\{TimeUtil.get_ctime()}_error.png')


            return False

    @classmethod
    def assert_equal_api(cls,actual,expect):
        if expect in actual:
            print("成功")
            return True
        else:
            print("失败")
            return False

    @classmethod
    def screen_shot(cls, driver, path):
        driver.get_screenshot_as_file(path)

if __name__ == '__main__':
    pass
    # UiUtil.click_image("t1.png")
    # UiUtil.click_image("t2.png")
    # UiUtil.keyboard.type_string("wo")
    # print(UiUtil.find_image("test.png"))
    # time.sleep(2)
    # for i in range(2):
    #     UiUtil.input_image("t2.png",f"nidaye{i}")
    #     time.sleep(0.01)
    #
    #     UiUtil.enter()
    # UiUtil.get_driver()
    # print(Api.request("post","http://172.16.13.30:8080/WoniuSales1.4/user/login/",{"username":"admin","password":"admin123","verifycode":"0000"}).text)
    print(Api.get_session())
    # print(FileUtil.get_ini("../conf/base.ini", "api", "login_data"))