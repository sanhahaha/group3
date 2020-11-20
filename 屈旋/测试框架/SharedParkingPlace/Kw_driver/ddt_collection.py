import os

from selenium import webdriver

from FrameDemo.SharedParkingPlace.Tool.file_uite import logutil


class Collection:

    logger = logutil.get_logger(os.path.join(os.getcwd(), 'collection'))
    driver = None

    @classmethod
    def open_browser(cls, browser):
        if hasattr(webdriver, browser):
            cls.driver = getattr(webdriver, browser)()
        else:
            cls.logger.error('浏览器名称不正确')
            cls.driver = webdriver.Firefox()

        cls.driver.implicitly_wait(5)
        # cls.driver.maximize_window()
        return cls.driver

    @classmethod
    def find_element(cls, attr):
        at = attr.split('=')
        element = None
        try:
            if at[0] == 'id':
                element = cls.driver.find_element_by_id(at[1])
            elif at[0] == 'link_text':
                element = cls.driver.find_element_by_link_text(at[1])
            elif at[0] == 'css_selector':
                element = cls.driver.find_element_by_css_selector(at[1])
            elif at[0] == 'xpath':
                element = cls.driver.find_element_by_xpath(at[1])
        except BaseException:
            cls.logger.error(f'没有找到{attr}元素')
        finally:
            return element

    @classmethod
    def get_page(cls, url):
        cls.driver.get(url)

    @classmethod
    def click(cls, attr):
        # 找到元素
        element = cls.find_element(attr)
        if element is not None:
            element.click()
        return element

    @classmethod
    def input(cls, attr, value):
        element = cls.click(attr)
        element.clear()
        element.send_keys(value)

    @classmethod
    def select(cls, attr, value):
        element = cls.click(attr)
        from selenium.webdriver.support.select import Select
        Select(element).select_by_visible_text(value)

    @classmethod
    def get_page_text(cls, attr):
        element = cls.find_element(attr)
        return element.text

    @classmethod
    def assert_exist_element(cls, attr):
        element = cls.find_element(attr)

        if element is not None:
            print('页面存在该元素，测试成功')
            result = '页面存在该元素，测试成功'
            if not os.path.exists(f'..\\Test_data\\result'):
                os.mkdir(f'..\\Test_data\\result')

            report_path = f'..\\Test_data\\result\\result.txt'
            with open(report_path, 'w', encoding='utf-8') as file:
                file.write(result)
                file.close()

        else:
            print('页面不存在该元素，测试失败')
            result = '页面不存在该元素，测试失败'
            if not os.path.exists(f'..\\Test_data\\result'):
                os.mkdir(f'..\\Test_data\\result')

            report_path = f'..\\Test_data\\result\\result.txt'
            with open(report_path, 'w', encoding='utf-8') as file:
                file.write(result)
                file.close()

    @classmethod
    def assert_equal(cls, attr, expect):
        actual = cls.get_page_text(attr)
        if expect == actual:
            print('测试通过')
            return True
        else:
            print('测试失败')
            return False

    @classmethod
    def sleep(cls, ctime):
        import time

        time.sleep(int(ctime))

    @classmethod
    def close(cls):
        cls.driver.quit()

    @classmethod
    def switch_to_alert(cls):
        cls.driver.switch_to.alert.accept()

    @classmethod
    def switch_iframe(cls,iframe):
        cls.driver.switch_to.frame(iframe)



