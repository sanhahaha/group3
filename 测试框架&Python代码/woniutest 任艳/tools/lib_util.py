# ui自动化操作的工具包      以及接口测试的包；
from pymouse import PyMouse   #鼠标
from pykeyboard import PyKePyboard #键盘；
import os
from selenium.webdriver.common.by import By


from pycharm.测试框架.woniutestV1.tools.util import LogUtil, FileUtil # 日志， 文件处理类

#接口测试的类；
class APIUtil:

    @classmethod
    def get_session(cls): #先调用了登录，获得登录产生的session？？？
        """
        获取具有权限的session
        :return: 带登录cookie的session
        """
        import requests
        session = requests.session()
        login_url = FileUtil.get_ini_value('..\\conf\\base.ini', 'api', 'login_url')
        login_data = eval(FileUtil.get_ini_value('..\\conf\\base.ini', 'api', 'login_data'))
        session.post(login_url, login_data)
        return session #获取session对象；
    # 向接口发送请求数据；
    @classmethod
    def request(cls, method, url, data=None): #需要使用方法值；url 和字典格式的参数；
        """
        发送请求获得响应
        :param method: 请求方式
        :param url: 请求url
        :param data: 请求数据
        :return: 响应结果
        """
        session = cls.get_session()
        resp = getattr(session, method)(url, params = data) #使用映射，，，方法和session连接起来； session.post（）
        # print(resp.text)
        return resp #返回响应结果；

    # 判断接口响应结果；传入的数据，是一个字典，，根据键名，取值，，判断响应的文本，和期望的文本值；
    @classmethod
    def assert_api(cls, test_info):
        for info in test_info:
            resp = APIUtil.request(info['request_method'], info['uri'], info['params'])
            #测试打印:后续删除
            print(info['request_method'], info['uri'], info['params'])
            # print(resp.text) #测试用打印：后续删除；
            Assert.assert_equal(resp.text, info['expect'])




# **********************************************************************************************
# ui自动化测试的工具包，
class UiUtil:

    driver = None
    logger = LogUtil.get_logger(os.path.join(os.getcwd(), 'ui_util')) #日志
    mouse = PyMouse() #鼠标封装的功能；
    keyboard = PyKeyboard() #键盘封装；

    # 生成driver，单例模式，任何时候调用这个方法，只会是一个driver;
    @classmethod
    def get_driver(cls):

        from selenium import webdriver
        try:
            browser = FileUtil.get_ini_value('..\\conf\\base.ini', 'ui', 'browser') #通过ini文件进行取值；得到浏览器信息，后面映射，
            base_url = FileUtil.get_ini_value('..\\conf\\base.ini', 'ui', 'homepage_url') #获得主页的url; 也就是登录主界面；
            if cls.driver is None:
                cls.driver = getattr(webdriver, browser)()
                cls.driver.implicitly_wait(5)
                cls.driver.maximize_window()
                cls.driver.get(base_url)
        except:
            cls.logger.error('浏览器对象生成错误，请检查配置文件')
        return cls.driver


    #查找元素的类：：：：：：：报黄颜色区域；
    @classmethod  #根据输入的section选择哪一块数据，，根据输入的option，作为键名，再去调用键值，键值是一个元组，根据下标取值；
    def find_elment(cls, section, option):  #键名和键值；用于下面的读取ini文件；是指定section下方所有的值；  这个option和下面的键取匹配；
        try:
            element_attr = FileUtil.get_ini_section('..\\conf\\inspector.ini',section) #元素的信息，存放在inspector.ini文件中；
            for element in element_attr: #循环取出每个小字典，小字典又是一个字典；
                if option in element.keys(): #判断所提供的参数中的 option,
                    attr = eval(element[option]) #取出字典的键名
            return cls.driver.find_element(getattr(By, attr[0]), attr[1]) #映射的方法，by,和id,和后面的值；
        except:                                   #获得的参数，其实一个是查找元素的方法，一个是填入的值；
            return None

    #更改时间选择变为文本输入的方法：
    @classmethod
    def choose_to_input(cls,):
        #重点语句********************
        js='document.getElementById("childdate").removeAttribute("readonly")'
        cls.driver.execute_script(js)


    #处理弹窗的方法；


    #  输入操作；参数， 元素，输入的值；
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

    # 点击操作， 参数，元素；
    @classmethod
    def click(cls, element):
        """
        点击某个元素
        :param element:任何一个元素对象
        :return:无
        """
        element.click()

    #选择下拉框，随机选择值；
    @classmethod
    def select_ro(cls, element):
        """
        随机选择下拉框中的某一项
        :param element: 下拉框元素对象
        :return: 无
        """
        from selenium.webdriver.support.select import Select
        import random
        random_index = random.randint(0, len(Select(element).options)-1)
        Select(element).select_by_index(random_index)
    # 选择下拉框，参数，下拉框元素怒，根据输入的文本值；
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



    # 图片比对；
    @classmethod
    def find_image(cls, target):

        image_path = '..\\image'
        screen_path = os.path.join(image_path,'screen.png') #image文件下方的 screen.png文件，
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
            return -1 ,-1

        x = max_loc[0] + int(template.shape[1] / 2)
        y = max_loc[1] + int(template.shape[0] / 2)
        return x, y #返回图像的中心点坐标；

    # 点击一张图，，，但是目前基本没有用到，
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
    # 双击图片；
    @classmethod
    def double_click_image(cls, target):
        x, y = cls.find_image(target)
        if x == -1 and y == -1:
            cls.logger.error(f'{target}图片未匹配')
            return
        cls.mouse.click(x, y, n=2)
    # 图片？？？
    @classmethod
    def input_image(cls, target, msg):
        x, y = cls.find_image(target)
        if x == -1 and y == -1:
            cls.logger.error(f'{target}图片未匹配')
            return
        cls.keyboard.type_string(msg)
    # 选择图片？？？
    @classmethod
    def select_image(cls, target, count):
        # 点击这个下拉框
        cls.click_image(target)
        # count次执行向下键
        for i in range(count):
            cls.keyboard.press_key(cls.keyboard.down_key)
        # 回车
        cls.keyboard.press_key(cls.keyboard.enter_key)
    # 截图？？已经封装好的方法；
    @classmethod
    def screen_shot(cls, driver, path):
        driver.get_screenshot_as_file(path)

# 断言类；
class Assert:
    # 判断期望值，前提，返回的是文本信息，test-pass或者fail;
    @classmethod
    def assert_equal(cls, expect, actual):
        if expect == actual:
            test_result = 'test-pass'
        else:
            test_result = 'test-fail'
        print(test_result)



if __name__ == '__main__':
    # print(UiUtil.find_image('debug.png'))
    # UiUtil.get_driver()
    # APIUtil.get_session()
    APIUtil.request('post', 'http://192.168.159.129:8080/WoniuSales/',
                    {"username": "admin", "password": "Milor123", "verifycode": "0000"})