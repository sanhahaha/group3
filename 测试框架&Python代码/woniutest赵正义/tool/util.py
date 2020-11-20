import os
import pymysql
class  TimeUtil:
    @classmethod
    def get_ctime(cls):
        """
           返回用于文件名格式的时间字符串
       :param :

       :return:
           时间字符串格式为%Y%m%d_%H%M%S
       """
        import time
        return time.strftime('%Y%m%d_%H%M%S', time.localtime())

    @classmethod
    def get_time(cls):  # 数据库里面用的时间
        """
                获取当前系统时间，返回标准格式时间
                :return: 返回的时间格式为%Y-%m-%d %H:%M:%S
        """
        import time
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())



class LogUtil:

    logger = None


    @classmethod
    def get_logger(cls, name):
        """
        生成日志文件
        信息级别：debug,info,warn,error
        :return:
        """
        import logging
        if cls.logger is None:
            # 获取日志生成器对象
            cls.logger = logging.getLogger(name)
            # 定义获取信息的级别
            cls.logger.setLevel(level=logging.INFO)
            # 如果日志目录不存在则创建
            if not os.path.exists('..\\logs'):
                os.mkdir('..\\logs')
            # 创建logger的文件句柄与规定的文件关联
            handler = logging.FileHandler('..\\logs\\'+TimeUtil.get_ctime()+'.log', encoding='utf8')
            # 定义信息的格式
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            cls.logger.addHandler(handler)

        log = os.listdir('..\\logs')
        if len(log) >= 10:
            for i in log:
                path_file = os.path.join('..\\logs', i)  # 取文件相对路径
                if os.path.isfile(path_file):
                    try:
                        os.remove(path_file)
                    except BaseException:
                        pass
                else:
                    continue

        return cls.logger
class FileUtil:
    logger = LogUtil.get_logger(os.path.join(os.getcwd(), 'util'))
    @classmethod
    def get_json(cls, path):
        """

        :param path: 路径
        :return: 返回一个json数据
        """
        # 获得日志生成器对象
        # logger = LogUtil.get_logger('openfile')
        import json5
        content = None
        try:
            with open(path, encoding='utf8') as file:
                content = json5.load(file)
            cls.logger.info('读取正确')
        except:
            cls.logger.error('文件读取错误')
        finally:
            # print(content)
            return content
    @classmethod
    def get_txt_line(cls,path):
        li = []
        print(path)
        with open(path, encoding='utf8') as file:
            file = file.readlines()
            for i in file:
                i=i.strip()
                if  not i.startswith("#"):
                    li.append(i)
        return li

    @classmethod
    def get_excel(cls, path, section, option):
        """
               从test_info.ini读取excel配置信息，将excel内容全部读出
               :param path:测试信息配置文件路径及文件名
               :param section: 页面名称
               :param option: 每条测试信息的键
               :return: 测试信息的json格式
               test_info_path:   xlsx路径
               sheet_name：   页面名字
                case_sheet_name  ：  版本号
                start_row：开始的行数
                end_row：   结尾的行数
                test_data_col：4   第四行  username=admin
                                        password=admin
                                        verifycode=0000
                expect_col：   5      login-sucess
                'caseid_col': 0, 'module_col': 1, 'type_col': 2, 'desc_col': 3   对应行数
               """
        params = eval(cls.get_ini(path, section, option))
        print(params)
        import xlrd

        workbook = xlrd.open_workbook(params['test_info_path'])
        sheet_content = workbook.sheet_by_name(params['sheet_name'])
        case_sheet_content = workbook.sheet_by_name(params['case_sheet_name'])
        version = case_sheet_content.cell(1, 1).value
        test_data = []

        for i in range(params['start_row'], params['end_row']):
            data = sheet_content.cell(i, params['test_data_col']).value
            expect = sheet_content.cell(i, params['expect_col']).value

            temp = str(data).split('\n')

            di = {}
            for t in temp:
                di[t.split('=')[0]] = t.split('=')[1]
            di['expect'] = expect
            di['caseid'] = sheet_content.cell(i, params['caseid_col']).value
            di['module'] = sheet_content.cell(i, params['module_col']).value
            di['type'] = sheet_content.cell(i, params['type_col']).value
            di['desc'] = sheet_content.cell(i, params['desc_col']).value
            di['version'] = version
            test_data.append(di)

        return test_data
    @classmethod
    def get_excel_api(cls, path, section, option):
        """
               {'params': {'username': 'admin', 'password': 'admin123', 'verifycode': '0000'},
               'expect': 'login-pass', 'caseid': 'login_api_01', 'module': '登录', 'type': 'api',
                'desc': '成功登录', 'version': 'V1.0', 'uri': 'http://172.16.13.30:8080/WoniuSales1.4/user/login/',
                 'request_method': 'post'}
         """
        params = eval(cls.get_ini(path, section, option))
        # print(params)
        import xlrd

        workbook = xlrd.open_workbook(params['test_info_path'])#'test_info_path': '..\\data\\ws_case_api.xlsx',
        sheet_content = workbook.sheet_by_name(params['sheet_name'])#'sheet_name': 'login',
        case_sheet_content = workbook.sheet_by_name(params['case_sheet_name'])#'case_sheet_name': 'caseinfo' 版本号
        version = case_sheet_content.cell(1, 1).value
        test_data = []
        # di = {}
        for i in range(params['start_row'], params['end_row']):#'start_row': 1, 'end_row': 4,
            data = sheet_content.cell(i, params['test_data_col']).value#'test_data_col': 6,
            expect = sheet_content.cell(i, params['expect_col']).value#'expect_col': 7,
            di = {}
            request_params = {}
            if data:
                # print(data)
                temp = str(data).split('\n')
            # print(temp)


                for t in temp:
                    request_params[t.split('=')[0]] = t.split('=')[1]
            di["params"] = request_params
            di['expect'] = expect
            di['caseid'] = sheet_content.cell(i, params['caseid_col']).value
            di['module'] = sheet_content.cell(i, params['module_col']).value
            di['type'] = sheet_content.cell(i, params['type_col']).value
            di['desc'] = sheet_content.cell(i, params['desc_col']).value
            di['version'] = version
            di["uri"] = sheet_content.cell(i, params['uri']).value
            di["request_method"] = sheet_content.cell(i, params['request_method']).value
            # di["uri"] =
            test_data.append(di)
        # print(di)
        return test_data

    @classmethod
    def get_excel_api_un(cls, path, section, option):
        """
               {'params': {'username': 'admin', 'password': 'admin123', 'verifycode': '0000'},
               'expect': 'login-pass', 'caseid': 'login_api_01', 'module': '登录', 'type': 'api',
                'desc': '成功登录', 'version': 'V1.0', 'uri': 'http://172.16.13.30:8080/WoniuSales1.4/user/login/',
                 'request_method': 'post'}
         """
        params = eval(cls.get_ini(path, section, option))
        # print(params)
        import xlrd

        workbook = xlrd.open_workbook(params['test_info_path'])#'test_info_path': '..\\data\\ws_case_api.xlsx',
        sheet_content = workbook.sheet_by_name(params['sheet_name'])#'sheet_name': 'login',
        case_sheet_content = workbook.sheet_by_name(params['case_sheet_name'])#'case_sheet_name': 'caseinfo' 版本号
        version = case_sheet_content.cell(1, 1).value
        test_data = []

        # di = {}
        for i in range(params['start_row'], params['end_row']):#'start_row': 1, 'end_row': 4,
            data = sheet_content.cell(i, params['test_data_col']).value#'test_data_col': 6,
            expect = sheet_content.cell(i, params['expect_col']).value#'expect_col': 7,
            di = {}
            request_params = {}
            a = []

            if data:
                # print(data)
                temp = str(data).split('\n')
            # print(temp)


                for t in temp:
                    request_params[t.split('=')[0]] = t.split('=')[1]
            di["params"] = request_params
            di['expect'] = expect
            di['caseid'] = sheet_content.cell(i, params['caseid_col']).value
            di['module'] = sheet_content.cell(i, params['module_col']).value
            di['type'] = sheet_content.cell(i, params['type_col']).value
            di['desc'] = sheet_content.cell(i, params['desc_col']).value
            di['version'] = version
            di["uri"] = sheet_content.cell(i, params['uri']).value
            di["request_method"] = sheet_content.cell(i, params['request_method']).value
            a.append(di)
            test_data.append(a)

        # print(test_data)
        return test_data
    @classmethod
    def get_txt(cls,path):
        with open(path, encoding='utf8') as file:
            file = file.read()
            return file
    @classmethod
    def get_ymal(cls, path):
        '''

        :param path:
        :return: 解析的是yaml文件
        '''
        import yaml
        try:
            with open(path, encoding='utf-8') as y:
                result = yaml.load(y, Loader=yaml.SafeLoader)#yaml的加载器  SafeLoader返回结果为字典类型
        except:
            cls.logger.error("yaml文件应该有问题可以看看")
        finally:
            return result

    @classmethod
    def get_ini(cls,path,section,option):
        """

        :param path:路径
        :param section:节点
        :param option: 节点下的键
        :return:解析ini文件
        """
        import configparser
        cp = configparser.ConfigParser()
        value = None
        # try:
        cp.read(path , encoding="utf-8-sig")
        value = cp.get(section,option)#param section:节点  option: 节点下的键  value键的值
        # except:
        #     cls.logger.error("读取文件失败")
        return  value
    @classmethod
    def get_ini_list(cls,path,section):
        """

        :param path: 文件路径
        :param section: 规定节点  使用的是items所以是节点下的所有数据  然后经过解析 返回一个列表列表套字典字典为
        :return: 返回一个列表   列表套字典字典为
        """
        import configparser
        cp = configparser.ConfigParser()
        li =[]
        try:
            cp.read(path,encoding="utf-8-sig")
            temp = cp.items(section)
            # print(temp)#列表套元组
            for t in temp:
                di = {}
                di[t[0]]=t[1]
                li.append(di)
        except:
            cls.logger.error("读取文件失败")
        finally:
            return li#通过解析  列表套字典

class db:
    logger = LogUtil.get_logger(os.path.join(os.getcwd(), 'util'))#os.path.join(os.getcwd(),'util')   路径-日志的名字
    def __init__(self,option):
        '''
        连接数据库初始化方法option  是('172.16.13.18', 'woniusales', 'root', '123456', "utf8")
        :param option:
        '''
        a=FileUtil.get_ini("..\\conf\\base.ini","mysql",f"{option}")
        # print(a)
        self.db_info =eval(a)
    # @classmethod
    def get_conn(self):
        conn = None
        try:
#连接数据库   db_info文件里面是连接的各个参数
            conn =pymysql.connect(host=self.db_info[0], database=self.db_info[1], user=self.db_info[2],
                                  password=self.db_info[3], charset=self.db_info[4])
        except:
            self.logger.error("数据库连接错误   检查连接数据")
        finally:

            return conn
    # @classmethod
    def query_one(self,sql):
        # db_info = eval(FileUtil.get_ini())#利用eval可以将字符串 装换成python语句
        conn = self.get_conn()
        cur = conn.cursor()#创建游标
        result = None
        try:
            cur.execute(sql)#执行sql语句
            result = cur.fetchone()#fetchone是一回只能返回一个数据
        except:
            self.logger.error('查询失败')
        finally:
            cur.close()
            conn.close()
            return result

    # @classmethod
    def query_all(self, sql):
        # db_info = eval(FileUtil.get_ini("../conf/base.ini", 'mysql', 'db_info'))  # 利用eval可以将字符串 装换成python语句
        conn = self.get_conn()
        cur = conn.cursor()  # 创建游标
        result = None
        try:
            cur.execute(sql)  # 执行sql语句
            result = cur.fetchall()#fetchone是一回返回所有数据
        except:
            self.logger.error('查询失败')
        finally:
            cur.close()
            conn.close()
            return result

    # @classmethod
    def update_db(self, sql):
        """
        增删改操作
        :param sql: DML语句
        :return:执行成功或失败的标记
        """
        flag = True
        # db_info = eval(FileUtil.get_ini('..\\conf\\base.ini', 'mysql', 'db_info'))
        conn = self.get_conn()
        cur = conn.cursor()
        try:
            cur.execute(sql)
            conn.commit()
        except:
            flag = False
            self.logger.error('sql执行失败')
        finally:
            cur.close()#关闭游标
            conn.close()#关闭连接
            return flag

if __name__ == '__main__':
    # t1=testfile()
    # print(t1.t1("../conf/woniu.json",0))
    # print(db.query_one('select role from user '))
    # print(FileUtil.get_ini_list("../conf/base.ini","host"))
    # print(FileUtil.get_ymal("../conf/ya.yaml"))
    # pass
    # a="#qwertyu"
    # print( not a.startswith("#"))
    pass
    # print(TimeUtil.get_ctime())
    # print(TimeUtil.get_time())
    # print(FileUtil.get_excel('..\\conf\\test_info.ini', 'login', 'login_info'))
    FileUtil.get_excel_api_un('..\\conf\\test_info.ini', 'car', 'caradd' )
    # print(FileUtil.get_ini("../conf/base.ini","mysql","db_info",))