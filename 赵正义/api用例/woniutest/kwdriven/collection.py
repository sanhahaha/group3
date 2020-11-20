import os




from selenium import webdriver

from woniutest.tool.util import LogUtil


class Collection:

    logger = LogUtil.get_logger(os.path.join(os.getcwd(), 'collection'))
    driver = None

    @classmethod
    def open_browser(cls, browser):
        if hasattr(webdriver, browser):
            cls.driver = getattr(webdriver, browser)()
        else:
            cls.logger.error('浏览器名称不正确')
            cls.driver = webdriver.Firefox()

        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
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
        except:
            cls.logger.error(f'没有找到{attr}元素')
        finally:
            return element

    @classmethod
    def get_page(cls, url):
        print(url)
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
        else:
            print('页面不存在该元素，测试失败')

    @classmethod
    def assert_equal(cls, attr, expect):
        actual = cls.get_page_text(attr)
        if expect == actual:
            print('测试通过')
        else:
            print('测试失败')

    @classmethod
    def queding(cls):  # 删除

        cls.driver.switch_to.alert.accept()  # 确定

    @classmethod
    def quxiao(cls):  # 内容
        cls.driver.switch_to.default_content()

    @classmethod
    def sleep(cls, ctime):
        import time

        time.sleep(int(ctime))

    @classmethod
    def close(cls):
        cls.driver.quit()



if __name__ == '__main__':
    c = Collection
    c.open_browser('Firefox')
    c.get_page('http://172.16.13.183:8888/WoniuSales1.4/')
    # c.input('id=username', 'admin')
    # c.input('id=password', 'Milor123')
    # c.input('id=verifycode', '0000')
    # c.click('xpath=/html/body/div[4]/div/form/div[6]/button')
    # c.sleep(2)
    # c.assert_exist_element('link_text=注销')
    # c.close()