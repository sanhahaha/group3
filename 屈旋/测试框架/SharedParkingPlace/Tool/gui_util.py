from FrameDemo.SharedParkingPlace.Tool.file_uite import logutil
from FrameDemo.SharedParkingPlace.Tool.file_uite import File_Uite
from selenium.webdriver.common.by import By
import os

class uiutil:
    driver = None
    logger = logutil.get_logger(os.path.join(os.getcwd(), 'gui_util'))

    @classmethod
    def find_element(cls,section,option):
        try:
            element_attr = File_Uite.get_ini_section('..\\Test_data\\inspector.ini', section)
            for element in element_attr:
                if option in element.keys():
                    attr = eval(element[option])
                    print(attr[1])
            return cls.driver.find_element(getattr(By, attr[0]), attr[1])
        except:
            return None

    @classmethod
    def get_driver(cls):
        from selenium import webdriver
        try:
            browser = File_Uite.get_ini_value('..\\Test_data\\base.ini','ui','browser')
            base_url = File_Uite.get_ini_value('..\\Test_data\\base.ini','ui','base_url')
            if cls.driver is None:
                cls.driver = getattr(webdriver,browser)()
                cls.driver.implicitly_wait(5)
                cls.driver.maximize_window()
                cls.driver.get(base_url)
        except:
            cls.logger.error("浏览器对象生成错误，请检查配置文件")
        finally:
            return cls.driver

    @classmethod
    def input(cls,web_object,value):
        '''
        对文本输入框执行点击、清理和输入值的动作
        :param txt_obj:
        :param value:
        :return: 无
        '''
        web_object.click()
        web_object.clear()
        web_object.send_keys(value)

    @classmethod
    def click(cls,element):
        '''
        点击某个元素
        :param element:  obj
        :return: 无
        '''
        element.click()


    @classmethod
    def select_ro(cls,element):
        '''
        随机选择下拉框的某一项
        :param element: 下拉框元素对象
        :return: 无
        '''
        from selenium.webdriver.support.select import Select
        import random
        random_index = random.randint(0, len(Select(element).options) - 1)  # 根据【选择，下拉框，这个选项】的长度
        Select(element).select_by_index(random_index)  # 选择按钮的下标 根据随机选项框数


    @classmethod
    def select_by_text(cls,element,text):
        '''
        根据下文本选择该项
        :param element:下拉框元素对象
        :param text: 元素的下标
        :return:
        '''
        from selenium.webdriver.support.select import Select
        Select(element).select_by_index(text)  # 选择按钮的下标




