from pymouse import PyMouse
from pykeyboard import PyKeyboard
import os

from selenium.webdriver.common.by import By

from woniutestV1.tools.util import LogUtil, FileUtil

class APIUtil:

    @classmethod
    def get_session(cls):                      # 已经完成了登录操作，拿到登录后的session
        """
        获取具有权限的session
        :return: 带登录cookie的session
        """
        import requests
        session = requests.session()
        session.get("http://192.168.226.146:8080/SharedParkingPlace/image")

        # login_url = FileUtil.get_ini_value('..\\conf\\base.ini', 'api', 'login_url')
        # login_data = eval(FileUtil.get_ini_value('..\\conf\\base.ini', 'api', 'login_data'))
        res=session.get("http://192.168.226.146:8080/SharedParkingPlace/login?uname=物业0&upass=123&imgcode=0000")
        print(res.text)
        return session

    @classmethod
    def request(cls, method, url, data=None):  # 拿到了上面的session
        """
        发送请求获得响应
        :param method: 请求方式
        :param url: 请求url
        :param data: 请求数据
        :return: 响应结果
        """
        session = cls.get_session()
        resp = getattr(session, method)(url, params = data)
        return resp

    @classmethod
    def assert_api(cls, test_info):

        for info in test_info:
            resp = APIUtil.request(info['request_method'], info['uri'], info['params'])
            Assert.assert_equal(resp.text, info['expect'])


# *****************************************************************************
class UiUtil:

    driver = None
    logger = LogUtil.get_logger(os.path.join(os.getcwd(), 'ui_util'))
    mouse = PyMouse()
    keyboard = PyKeyboard()

    @classmethod
    def get_driver(cls):

        from selenium import webdriver
        try:
            browser = FileUtil.get_ini_value('..\\conf\\base.ini', 'ui', 'browser')
            base_url = FileUtil.get_ini_value('..\\conf\\base.ini', 'ui', 'homepage_url')
            if cls.driver is None:
                cls.driver = getattr(webdriver, browser)()
                cls.driver.implicitly_wait(5)
                cls.driver.maximize_window()
                cls.driver.get(base_url)
        except:
            cls.logger.error('浏览器对象生成错误，请检查配置文件')
        return cls.driver


    @classmethod
    def find_element(cls,section,option):
        try:
            element_attr = FileUtil.get_ini_section('..\\conf\\inspector.ini', section)
            for element in element_attr:
                if option in element.keys():
                    attr = eval(element[option])
                    print(attr[1])
            return cls.driver.find_element(getattr(By, attr[0]), attr[1])
        except:
            return None

    @classmethod
    def input(cls, element, value):
        """
        对文本输入框执行点击、清理和输入值的动作
        :param element:文本元素对象
        :param value:向文本框输入的值
        :return:无
        """
        element.click()
        element.clear()
        element.send_keys(value)

    @classmethod
    def click(cls, element):
        """
        点击某个元素
        :param element:任何一个元素对象
        :return:无
        """
        element.click()

    @classmethod
    def select_randomly(cls, element):
        """
        随机选择下拉框中的某一项
        :param element: 下拉框元素对象
        :return: 无
        """
        from selenium.webdriver.support.select import Select
        import random
        random_index = random.randint(0, len(Select(element).options)-1)
        Select(element).select_by_index(random_index)

    @classmethod
    def select_by_text(cls, element, text):
        """
        根据下拉文本选择该项
        :param element: 下拉框元素对象
        :param text: 可见的文本
        :return:无
        """
        from selenium.webdriver.support.select import Select
        Select(element).select_by_visible_text(text)

    @classmethod
    def find_image(cls, target):

        image_path = '..\\image'
        screen_path = os.path.join(image_path,'screen.png')
        from PIL import ImageGrab
        ImageGrab.grab().save(screen_path)

        # 读取大图对象
        import cv2
        screen = cv2.imread(screen_path)
        # 读取小图对象
        template = cv2.imread(os.path.join(image_path,target))
        # 进行模板匹配，参数包括大图对象、小图对象和匹配算法
        result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        # 获取匹配结果
        min, max, min_loc, max_loc = cv2.minMaxLoc(result)

        similarity = FileUtil.get_ini_value('..\\conf\\base.ini', 'imagematch', 'similarity')
        if max < float(similarity):
            return -1 ,-1     #没匹配到返回 -1 -1

        x = max_loc[0] + int(template.shape[1] / 2)
        y = max_loc[1] + int(template.shape[0] / 2)
        return x, y          # 匹配成功 返回图片的对角线坐标

    @classmethod
    def click_image(cls, target):
        """
        单击一张图片
        :param target:
        :return:
        """
        x, y = cls.find_image(target)
        if x == -1 and y == -1:
            cls.logger.error(f'{target}图片未匹配')
            return
        cls.mouse.click(x, y)

    @classmethod
    def double_click_image(cls, target):
        x, y = cls.find_image(target)
        if x == -1 and y == -1:
            cls.logger.error(f'{target}图片未匹配')
            return
        cls.mouse.click(x, y, n=2)

    @classmethod
    def input_image(cls, target, msg):     #截的是输入框，输入内容
        x, y = cls.find_image(target)
        if x == -1 and y == -1:
            cls.logger.error(f'{target}图片未匹配')
            return
        cls.keyboard.type_string(msg)

    @classmethod
    def select_image(cls, target, count):  #截的是下拉框，点击小按钮，选择
        # 点击这个下拉框
        cls.click_image(target)
        # count次执行向下键
        for i in range(count):
            cls.keyboard.press_key(cls.keyboard.down_key)
        # 回车
        cls.keyboard.press_key(cls.keyboard.enter_key)

    @classmethod
    def screen_shot(cls, driver, path):   #截图
        driver.get_screenshot_as_file(path)

class Assert:

    @classmethod
    def assert_equal(cls, expect, actual):
        if expect == actual:
            test_result = 'test-pass'
        else:
            test_result = 'test-fail'
        print(test_result)



if __name__ == '__main__':
    APIUtil.get_session()
