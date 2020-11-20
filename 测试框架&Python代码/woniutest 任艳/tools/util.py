import time
import os
import configparser

# 时间类
class TimeUtil:

    #字符串格式时间；
    @classmethod
    def get_filename_time(cls):
        """
           返回用于文件名格式的时间字符串
       :param :

       :return:
           时间字符串格式为%Y%m%d_%H%M%S
       """
        return time.strftime('%Y%m%d_%H%M%S', time.localtime())

    #标准格式时间；
    @classmethod
    def get_standard_format_time(cls):
        """
        获取当前系统时间，返回标准格式时间
        :return: 返回的时间格式为%Y-%m-%d %H:%M:%S
        """

        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

# *********************************************************************************************
# 日志生成类
class LogUtil:

    logger = None
    #生成日志对象；
    @classmethod
    def get_logger(cls, name):
        """
            返回规定格式的日志生成器对象
        :param name:
            调用logger的模块名
        :return:
            日志生成器对象
        """
        import logging

        if cls.logger is None:
            cls.logger = logging.getLogger(name)
            cls.logger.setLevel(level=logging.INFO)
            if not os.path.exists('..\\logs'):
                os.mkdir('..\\logs')
            handler = logging.FileHandler(
                '..\\logs\\' + TimeUtil.get_filename_time() + '.log', encoding='utf8')
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            cls.logger.addHandler(handler)
            cls.logger.info('*****************************************************\n')

        return cls.logger

# *****************************************************************************************

# 文件处理类；
class FileUtil:

    # 该类包含所有文件读取方法，包括从普通文本、json格式文本、excel文件中读取的相关方法
    logger = LogUtil.get_logger(os.path.join(os.getcwd(), 'util'))
    # 读取普通文本；参数：放置文本文件得路径，
    @classmethod
    def get_txt(cls, path):
        """
        读取普通文本文件内容，返回字符串
        :param path: 文本文件路径
        :return: 文本文件内容字符串
        """
        content = None
        try:
            with open(path, encoding='utf-8') as file:
                content = file.read()
        except:
            cls.logger.error(f'没有读取{path}文件')
        finally:
            return content
    # 读取文本文件，但是返回，列表+字符串得格式，，参数：放置文本文件得路径；
    @classmethod
    def get_txt_line(cls, path):
        """
        按行读取文本内容，返回列表+字符串格式
        :param path: 文本路径
        :return: 列表+字符串（不包含换行，去掉#开始的行内容）
        """
        li = []
        try:
            with open(path, encoding='utf-8') as file:
                contents = file.readlines()

            for content in contents:
                if not content.startswith('#'):
                    t = content.strip()
                    li.append(t)
        except:
            cls.logger.error(f'没有读取{path}文件')
        finally:
            return li
    # 读取json格式的文件，参数，放置json文件的路径；
    @classmethod
    def get_json(cls, path):
        """
            从json格式文件中读取原始格式内容并返回
        :param path:
            要读取的json文件路径
        :return:
            原始数据类型的数据
        """

        import json5
        content = None
        try:
            with open(path, encoding='utf8') as file:
                content = json5.load(file)
        except BaseException:
            cls.logger.error(f'{path}文件读取错误')
        finally:
            return content
    # 读取 excel 文件，但是该文件的地址以及读取的行和列的内容，都是写在另一个文件夹里面，使用读取ini文件的方式，地址，是base.ini文件，section和option
    @classmethod
    def get_test_info(cls, path, section, option):
        """
        从test_info.ini读取excel配置信息，将excel内容全部读出
        :param path:测试信息配置文件路径及文件名
        :param section: 页面名称
        :param option: 每条测试信息的键
        :return: 测试信息的json格式
        """
        #使用了eval进行转换；注意这个方法；
        params = eval(cls.get_ini_value(path, section, option)) #ini文件读取出来是一个字典；pip install  xlrd
        import xlrd

        workbook = xlrd.open_workbook(params['test_info_path']) #打开excel文件的地址，是通过 字典+键名 进行取值；把需要的几个重要参数，比如开始行，结束行，数据行，期望值行，均通过键值对的方式取出来；
        sheet_content = workbook.sheet_by_name(params['sheet_name'])
        case_sheet_content = workbook.sheet_by_name(params['case_sheet_name'])
        version = case_sheet_content.cell(1, 1).value #从excel的第一页取出了文件的版本号；
        test_data = [] #定义大字典；后续每一组数据，作为一个元素，装在给列表中；

        for i in range(params['start_row'], params['end_row']): #循环，从，起始行到结束行；
            data = sheet_content.cell(i, params['test_data_col']).value #在每一行循环的基础上，取出想要的列中的信息；
            expect = sheet_content.cell(i, params['expect_col']).value #上面取数据，这行取期望结果；
            temp = str(data).split('\n')
            di = {}
            request_params = {} # 用于保存发送接口传递的参数
            for t in temp:
                request_params[t.split('=')[0]] = t.split('=')[1] #等号前后的值，作为一个键值对；
            di['params'] = request_params
            di['expect'] = expect
            di['caseid'] = sheet_content.cell(i, params['caseid_col']).value
            di['module'] = sheet_content.cell(i, params['module_col']).value
            di['type'] = sheet_content.cell(i, params['type_col']).value
            di['desc'] = sheet_content.cell(i, params['desc_col']).value
            di['version'] = version
            di['uri'] = sheet_content.cell(i, params['uri']).value #如果没有url，会不会报错；：：：：
            di['request_method'] = sheet_content.cell(i, params['request_method']).value
            test_data.append(di) #大列表中； 一组数据，是一个字典；
        return test_data
    # 读取ini文件中，对应option的值；；参数，ini文件的地址，section用于确定数据区域，option用于取具体的值；
    @classmethod
    def get_ini_value(cls, path, section, option):
        """
        从ini配置文件中读取某个指定的键对应的值并返回
        :param path:配置文件路径
        :param section:节点名称
        :param option:键的名称
        :return:对应的单值
        """

        cp = configparser.ConfigParser()
        value = None
        try:
            cp.read(path, encoding='utf-8')
            value = cp.get(section, option)
        except BaseException:
            cls.logger.error('读取配置文件错误')
        return value
    # 读取ini文件中，对应section 下方的所有的option的值；以字典格式返回，使用时候可进行打印；
    @classmethod
    def get_ini_section(cls, path, section):
        """
        从ini配置文件中读取某个节点下的所有内容，以字典格式返回
        :param path:
        :param section:
        :return:
        """

        cp = configparser.ConfigParser()
        li = []
        try:
            cp.read(path, encoding='utf-8-sig')
            temp = cp.items(section)
            for t in temp:
                di = {}
                di[t[0]] = t[1]
                li.append(di)
        except BaseException:
            cls.logger.error('读取配置文件错误')
        finally:
            return li

# *******************************************************************************
# 数据库处理类；database db
class DBUtil:

    # 该类包含数据库连接方法，查询单条数据方法，查询多条数据方法和增删改方法
    logger = LogUtil.get_logger(os.path.join(os.getcwd(), 'util'))  #当前路径下的 util模块； 获取当前路径，然后在当前路径下找 util这个模块；

    def __init__(self, option): #初始化，从base.ini文件中获取 数据库连接的配置信息，服务器ip,用户名，密码等参数

        self.db_info = eval(
            FileUtil.get_ini_value(
                '..\\conf\\base.ini',
                'mysql',
                f'{option}')) #上面的 mysql决定了使用数据库的信息区域，下面的option决定使用哪个数据库的配置信息；

    def get_conn(self): #获得打开数据的对象；
        """
        连接数据库返回数据库连接对象
        :param db_info:数据库配置信息
        :return:数据库连接对象
        """
        import pymysql
        conn = None
        try: # 使用下标对读取ini文件进行取值；
            conn = pymysql.connect(
                host=self.db_info[0],
                user=self.db_info[1],
                password=self.db_info[2],
                database=self.db_info[3],
                charset=self.db_info[4])
        except BaseException:
            self.logger.error('数据库连接失败')
        finally:
            return conn
    # 查询一条数据库结果； 参数，参训sql语句；
    def query_one(self, sql):
        """
        查询一条结果
        :param sql: 查询语句
        :return: 单条结果集，以元组方式返回
        """

        conn = self.get_conn()
        cur = conn.cursor()
        result = None
        try:
            cur.execute(sql)
            result = cur.fetchone() #
        except BaseException:
            self.logger.error('查询失败')
        finally:
            cur.close()
            conn.close()
            return result
    # 查询多条数据库结果； 参数，查询的sql语句；
    def query_all(self, sql):
        """
        查询多条结果
        :param sql: 查询语句
        :return: 多条结果集，以二维元组方式返回
        """

        conn = self.get_conn()
        cur = conn.cursor()
        result = None
        try:
            cur.execute(sql)
            result = cur.fetchall()
        except BaseException:
            self.logger.error('查询失败')
        finally:
            cur.close()
            conn.close()
            return result

    # 更新数据库； 参数，比如填写数据的sql语句； 返回值，提交成功了返回 true,错误返回false;
    def update_db(self, sql):
        """
        增删改操作
        :param sql: DML语句
        :return:执行成功或失败的标记
        """
        flag = True

        conn = self.get_conn()
        cur = conn.cursor()
        try:
            cur.execute(sql)
            conn.commit()
        except BaseException:
            flag = False
            self.logger.error('sql执行失败')
        finally:
            cur.close()
            conn.close()
            return flag

if __name__ == '__main__':
    print(FileUtil.get_test_info('..\\conf\\test_info.ini', 'login', 'login_info_ui'))