# 1.从指定路径中读取普通文本内容，普通文本内容为多行字符串；
from woniutest.tool.util import LogUtil, FileUtil

import os
def get_txt(cls, path):
    with open(path, encoding='utf8') as file:
        file = file.read()
        return file
# 以遍历方式读取指定位置的excel文件中某个sheet页内的全部内容；


def get_json( path):
    logger = LogUtil.get_logger(os.path.join(os.getcwd(), 'util'))
    # 获得日志生成器对象
    # logger = LogUtil.get_logger('openfile')
    import json
    content = None
    try:
        with open(path, encoding='utf8') as file:
            content = json.load(file)
        logger.info('读取正确')
    except:
        logger.error('文件读取错误')
    finally:
        # print(content)
        return content
def get_excel(path,sheet):
    import xlrd
    workbook = xlrd.open_workbook(path)
    sheet_content = workbook.sheet_by_name(sheet)
    temp=[]
    for j in range(sheet_content.ncols):

            test_data = sheet_content.col_values(j)
            temp.append(test_data)

    return temp
# 获取logger对象方法；
def get_logger(name):
    """
    生成日志文件
    信息级别：debug,info,warn,error
    :return:
    """
    logger = None
    import logging
    if logger is None:
        # 获取日志生成器对象
        logger = logging.getLogger(name)
        # 定义获取信息的级别
        logger.setLevel(level=logging.INFO)
        # 如果日志目录不存在则创建
        if not os.path.exists('..\\logs'):
            os.mkdir('..\\logs')
        # 创建logger的文件句柄与规定的文件关联
        import time
        handler = logging.FileHandler('..\\logs\\' + time.strftime('%Y%m%d_%H%M%S', time.localtime()) + '.log', encoding='utf8')
        # 定义信息的格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger
# 读取ini文件的两个方法（指定节点内容，指定键对应的值）；
def get_ini(path,section,option):
    """

    :param path:路径
    :param section:节点
    :param option: 节点下的键
    :return:
    """
    import configparser
    cp = configparser.ConfigParser()
    value = None

    cp.read(path , encoding="utf-8")
    value = cp.get(section,option)

    return  value

def get_ini_list(path,section):
    """

    :param path: 文件路径
    :param section: 规定节点  使用的是items所以是节点下的所有数据  然后经过解析 返回一个列表列表套字典字典为
    :return: 返回一个列表   列表套字典字典为
    """
    import configparser
    cp = configparser.ConfigParser()
    li =[]
    cp.read(path,encoding="utf-8-sig")
    temp = cp.items(section)
    for t in temp:
        di = {}
        di[t[0]]=t[1]
        li.append(di)
    return li
# 使用反射获取webdriver的driver对象；
def get_driver():
    driver = None
    from selenium import webdriver
    browser = FileUtil.get_ini("../conf/base.ini","ui","browser")
    print(browser)
    if driver is None:
        driver = getattr(webdriver,browser)()
        driver.implicitly_wait(5)
        driver.maximize_window()
    return driver
def get_ymal(path):
    import yaml
    with open(path,encoding='utf-8') as y:
        result = yaml.load(y.read(),Loader=yaml.SafeLoader)
    return result
if __name__ == '__main__':
    print(get_excel("../data/ws_case_ui.xlsx","login"))
    # get_driver()
    # print(get_ymal("../conf/ya.yaml"))