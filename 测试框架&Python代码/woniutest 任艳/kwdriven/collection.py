# 用来封装界面各个元素的操作；和字典库intepret，以及脚本script里面的信息是对应的；

import os
from selenium import webdriver
from woniutestV1.tools.util import LogUtil,DBUtil


class Collection:
    #自己写的两行，可删除；
    result_first = 0
    result_second = 0


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
    def get_page_text(cls, attr): #获取元素的文本值；
        element = cls.find_element(attr)
        return element.text

    @classmethod #判断是否存在元素；
    def assert_exist_element(cls, attr):
        element = cls.find_element(attr)
        if element is not None:
            print('页面存在该元素，测试成功')
        else:
            print('页面不存在该元素，测试失败')

    @classmethod #判断期望值和实际值是否相等；
    def assert_equal(cls, attr, expect):
        actual = cls.get_page_text(attr)
        if expect == actual:
            print('测试通过')
        else:
            print('测试失败')

    @classmethod
    def sleep(cls, ctime):
        import time

        time.sleep(int(ctime))

    @classmethod
    def accept_box(cls):
        cls.driver.switch_to.alert.accept()


    @classmethod #关闭浏览器；
    def close(cls):
        cls.driver.quit()

#****************数据库两次查询结果比对*******************************
    @classmethod
    def database_query_first(cls,sql):
        result_temp = DBUtil('db_info').query_one(sql)
        cls.result_first = int(result_temp[0])
        print(cls.result_first)

    @classmethod
    def database_query_second(cls,sql):
        result_temp = DBUtil('db_info').query_one(sql)
        cls.result_second = int(result_temp[0])
        print(cls.result_second)

    @classmethod
    def judge_data(cls):
        if cls.result_first - cls.result_second == 1:

            print("数据库比对成功")
        else:
            print("数据库比对失败")

# ****************数据库两次查询结果比对*******************************

if __name__ == '__main__':
    c = Collection
    c.open_browser('Firefox')
    c.get_page('http://192.168.159.129:8080/WoniuSales/')
    c.input('id=username', 'admin')
    c.input('id=password', 'Milor123')
    c.input('id=verifycode', '0000')
    c.click('xpath=/html/body/div[4]/div/form/div[6]/button')
    c.sleep(2)
    c.assert_exist_element('link_text=注销')
    c.close()