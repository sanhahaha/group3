import os
import configparser


class logutil:
    logger = None
    # 日志

    @classmethod
    def get_ctime(cls):
        '''
            返回规定格式的时间字符串
        :params:
        :return:
            时间字符串格式为%Y%m%d_%H%M%S
        '''
        import time
        return time.strftime('%Y%m%d_%H%M%S', time.localtime())

    # 常驻内存 改为单例模式

    @classmethod
    def get_time(cls):
        '''
        获取当前系统时间，返回标准格式时间
        :return: 返回的时间格式为%y-%m-%d %H:%M:%S
        '''
        import time
        return time.strftime('%y-%m-%d %H:%M:%S', time.localtime())

    @classmethod
    def get_logger(cls, name):
        '''
            生成日志文件
            信息级别：debug,info,warn,error
            :return:
        '''

        import logging  # 生成日志
        import os
        if cls.logger is None:
            cls.logger = logging.getLogger(name)  # 获取日志生成器对象
            cls.logger.setLevel(level=logging.INFO)  # 定义获取信息的级别

            if not os.path.exists('..\\Logs'):  # 如果目录文件并不存在则创建
                os.mkdir('..\\Logs')
            handler = logging.FileHandler(
                '..\\Logs\\' + cls.get_ctime() + '.log',
                encoding='utf8')  # 创建loggger的文件句柄与规定的文件关联
            # 定义信息的格式 系统 模块  等级信息 具体打印的信息
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)  # 收集信息
            cls.logger.addHandler(handler)  # 添加信息
            cls.logger.info(
                '*****************************************************\n')
        return cls.logger


class File_Uite:
    # 该类包含所有文件读取方法，包括从普通文本、json格式文本、excel文件中读取的相关方法
    logger = logutil.get_logger(os.path.join(os.getcwd(), 'File_Uite'))

    @classmethod
    def get_txt(cls, path):
        """
            读取普通文本文件内容，返回字符串
            :param path: 文本文件路径
            :return: 文本文件内容字符串
        """
        with open(path, encoding='utf8') as a_txt:
            file = a_txt.read()
            return file


    @classmethod
    def get_txt_line(cls, path):
        """
            读取普通文本文件内容，返回字符串
            :param path: 文本文件路径
            :return: 文本文件内容字符串
        """
        with open(path, encoding='utf8') as a_txt:
            contents = a_txt.readlines()
            print(contents)
        li = []
        for content in contents:
            if not content.startswith('#'):
                temp = content.strip()
                li.append(temp)
        return li

    @classmethod
    def read_json(cls, path):
        """
            读取普通文本文件内容，返回字符串
            :param path: 文本文件路径
            :return: 文本文件内容字符串
        """
        logger = logutil.get_logger(
            os.path.join(
                os.getcwd(),
                'File_util_read_json'))   # 获得日志生成器对象
        import json5
        get_json = None
        try:
            with open(path, encoding='utf8') as file:
                get_json = json5.load(file)
            logger.info('read_json文件读取正确')
        except BaseException:
            logger.error('read_json文件读取错误')
        finally:
            return get_json


    @classmethod
    def read_excel_value(cls, path, section):
        '''
        从Excel中读取测试数据及预期结果；用配置文件获取参数
        从excel文件中读取测试信息
        :param path:测试信息配置文件路径及文件名
        :param index: 测试信息索引下标
        :return: 测试信息的json格式
        类型：说明
        '''
        params = cls.get_ini_section(path, section)
        import xlrd
        wn_case = xlrd.open_workbook(params[0]['path'])  # 读取Excel文件
        wn_contennt = wn_case.sheet_by_name(
            params[1]['sheet_name'])  # 读取sheet页的内容
        login_data = []
        for i in range(int(params[2]['start_row']),
                       int(params[3]['end_row'])):  # 行
            test_caseid = wn_contennt.cell(
                i,int(params[4]['caseid_col'])).value

            test_module = wn_contennt.cell(
                i,int(params[5]['module_col'])).value

            test_type = wn_contennt.cell(
                i, int(params[6]['type_col'])).value

            test_uri = wn_contennt.cell(
                i, int(params[7]['uri_col'])).value

            test_remethod = wn_contennt.cell(
                i, int(params[8]['remethod_col'])).value

            test_desc = wn_contennt.cell(
                i, int(params[9]['desc_col'])).value

            test_data = wn_contennt.cell(
                i, int(params[10]['data_col'])).value  # 列

            expect_result = wn_contennt.cell(
                i, int(params[11]['expect_col'])).value
            di = {}
            di['caseid'] = test_caseid
            di['module'] = test_module
            di['type'] = test_type
            di['uri'] = test_uri
            di['remethod'] = test_remethod
            di['desc'] = test_desc
            di['params'] = test_data
            di['expect'] = expect_result

            version = wn_case.sheet_by_name(
                params[12]['sheet_name_version_col'])  # 读取版本的内容

            for i in range(int(params[13]['version_start_row']),
                           int(params[14]['version_end_row'])):  # 行
                test_version_col = version.cell(
                    i, int(params[15]['version_col'])).value
                di['version'] = test_version_col
            login_data.append(di)

        return login_data

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
            cls.logger.error('get_ini_value 读取配置文件错误')
        finally:
            return value

    @classmethod
    def get_ini_section(cls, path, section):
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
            cls.logger.error('get_ini_section读取配置文件错误')
        finally:
            return li

    @classmethod
    def read_yaml(cls, path, write_filepath):
        '''

        yaml格式文件的读取方法并封装方法。
        :param path: 读取yaml文件路径
        :param write_filepath: 写入yaml文件路径
        '''
        with open(path, encoding="utf8") as yaml_file:
            yame_obj = yaml_file.read()
        import yaml
        # str_yaml_file ---> dict
        print(yaml.safe_load(yame_obj))

        # dict ---> str_yaml_object
        dict_var = {'name': 'Cactus', 'age': 18, 'skills': [
            ['Python', 3], ['Java', 5]], 'has_blog': True, 'gf': None}
        print(yaml.dump(dict_var, ))  # 转为字符串，使用默认flow流格式
        with open(write_filepath, 'w', encoding='utf-8') as f:
            yaml.dump(dict_var, f, default_flow_style=False)  # 写入文件


class db_Util:
    '''
        1.连接数据库
        2.查询数据库单条DQL
        3.查询数据库多条
        4.增删改 DML
    '''
    logger = logutil.get_logger(
        os.path.join(
            os.getcwd(),
            'db_Util'))  # 获得日志生成器对象
    # 不定常参数
    # eval用来执行一个字符串表达式

    def __init__(self, option):
        self.db_info = eval(
            File_Uite.get_ini_value(
                '..\\Test_data\\base.ini',
                'mysql',
                f'{option}'))

    def get_conn(self, db_info):
        '''
        配置文件中使用参数
        连接数据库返回数据库连接对象
        :param hostname:
        :param dbname:
        :param username:
        :param pwd:
        :return:
        hostname,dbname,username,pwd,charset
        '''
        import pymysql
        conn = None
        try:
            if conn is None:
                conn = pymysql.connect(
                    host=db_info[0],
                    database=db_info[1],
                    user=db_info[2],
                    password=db_info[3],
                    charset=db_info[4],
                    port=db_info[5])
        except BaseException:
            self.logger.error("get_conn 数据库连接失败")
            print('数据库连接失败')
        finally:
            return conn

    def query_one(self, sql):
        """
            查询一条结果
            :param sql: 查询语句
            :return: 单条结果集，以元组方式返回
        """
        conn = self.get_conn(self.db_info)
        cur = conn.cursor()
        result = None
        try:
            cur.execute(sql)
            result = cur.fetchone()
        except BaseException:
            self.logger.error("query_one 数据库单条语句查询失败！")
        finally:
            cur.close()
            conn.close()
            return result

    def query_all(self, sql):
        """
        查询多条结果
        :param sql: 查询语句
        :return: 多条结果集，以二维元组方式返回
        """
        conn = self.get_conn(self.db_info)
        cur = conn.cursor()
        result = None
        try:
            cur.execute(sql)
            result = cur.fetchall()
        except BaseException:
            self.logger.error("query_all 数据库多条语句查询失败！")
        finally:
            cur.close()
            conn.close()
            return result

    def update_db(self, sql):
        """
        增删改操作
        :param sql: DML语句
        :return:执行成功或失败的标记
        """
        result = True
        conn = self.get_conn(self.db_info)
        cur = conn.cursor()
        try:
            cur.execute(sql)
            conn.commit()
        except BaseException:
            result = False
            self.logger.error("update_db fall！")
            print('写入数据库失败')
        finally:
            cur.close()
            conn.close()
            return result


if __name__ == '__main__':
    print(File_Uite().read_excel_value("../Test_data/test_info.ini",'api_share'))
