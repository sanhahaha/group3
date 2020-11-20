from FrameDemo.SharedParkingPlace.Tool.file_uite import logutil, File_Uite,db_Util

import time
import os


class TestReport:
    def __init__(self, item_name):
        self.item_name = item_name  # 表名
        self.logger = logutil.get_logger('test_report')

    def write_report_db(self, result_info):  # 写入数据库

        now = logutil.get_time()

        sql = f'insert into {self.item_name}(version,' \
              f'module,case_type,case_id,case_desc,case_result,' \
              f'execute_time,error_msg,error_sceenshot,uri,requests_method,parame,expect)' \
              f'values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s");' \
              % (result_info[0], result_info[1], result_info[2],
                 result_info[3], result_info[4], result_info[5],
                 f'{now}', result_info[6], result_info[7], result_info[8],
                 result_info[9], result_info[10], result_info[11])

        # % (result_info['version'], result_info['module'], result_info['case_type'],
        #    result_info['case_id'], result_info['case_desc'], result_info['case_result'],
        #    f'{now}', result_info['error_msg'], result_info['error_sceenshot'], result_info['uri'],
        #    result_info['requests_method'], result_info['parame'], result_info['expect'])
        # 写入的是字典result_info = {'version':"v1.0"}
        print(sql)

        db_Util('db_report').update_db(sql)  # 配置文件键名（里面有库名） sql

    def generate_html_report(self, version):  # 查询数据库  写入替换报告 保存在指定的位置

        # 根据不同的版本读取该版本的测试结果数据
        sql_all = f'select * from {self.item_name} where version="{version}"'
        all_result = db_Util('db_report').query_all(sql_all)
        if len(all_result) == 0:
            print('没有该版本的测试结果')
            self.logger.info('没有该版本的测试结果')
            return
        sql_all_result = f'select count(*) from {self.item_name} where version="{version}"'
        all_results = db_Util('db_report').query_one(sql_all_result)[0]

        # 计算测试执行成功的数量
        sql_success = f'select count(*) from {self.item_name} where version="{version}" and case_result="test-pass"'
        sucess_result = db_Util('db_report').query_one(sql_success)[0]
        # 计算测试执行失败的数据
        sql_fail = f'select count(*) from {self.item_name} where version="{version}" and case_result="test-fail"'
        fail_result = db_Util('db_report').query_one(sql_fail)[0]
        # 计算测试执行错误的数据
        sql_error = f'select count(*) from {self.item_name} where version="{version}" and case_result="test-error"'
        error_result = db_Util('db_report').query_one(sql_error)[0]

        # 获取最后一条用例执行的时间
        lasttime_sql = f'select execute_time from {self.item_name} order by execute_time desc limit 0,1'
        lasttime = str(db_Util('db_report').query_one(lasttime_sql)[0])

        # 获取日期
        test_data = lasttime.split(' ')[0]

        result_str = ''
        for result in all_result:
            if result[6] == 'test-pass':
                color = 'blue'
            elif result[6] == 'test-fail':
                color = 'red'
            else:
                color = 'yellow'
            if result[9] == '无':
                screenshot = '无'
            else:
                screenshot = f'<a href="{result[9]}">查看截图</a>'

            # 表格中添加内容
            result_str += f'<tr height="40">' \
                f'<td width="5%">{result[0]}</td>' \
                f'<td width="7%">{result[2]}</td>' \
                f'<td width="7%">{result[3]}</td>' \
                f'<td width="5%">{result[4]}</td>' \
                f'<td width="12%">{result[5]}</td>' \
                f'<td width="6%" bgcolor="{color}">{result[6]}</td>' \
                f'<td width="12%">{result[7]}</td>' \
                f'<td width="12%">{result[8]}</td>' \
                f'<td width="7%">{result[10]}</td>' \
                f'<td width="5%">{result[11]}</td>' \
                f'<td width="5%">{result[12]}</td>' \
                f'<td width="7%">{result[13]}</td>' \
                f'<td width="10%">{screenshot}</td>' \
                f'</tr>\r\n'

            # 替换模板上特定位置的字符串
            with open('../Tool\\template.html', encoding='utf-8') as file:
                contents = file.read()

            contents = contents.replace('$test-date', test_data)
            contents = contents.replace('$test-version', version)
            contents = contents.replace('$cases-count', str(all_results))
            contents = contents.replace('$pass-count', str(sucess_result))
            contents = contents.replace('$fail-count', str(fail_result))
            contents = contents.replace('$error-count', str(error_result))
            contents = contents.replace('$last-time', lasttime)
            contents = contents.replace('$test-result', result_str)
        # 将内容写入新的测试报告中
        if not os.path.exists(f'..\\Report\\{version}'):
            os.mkdir(f'..\\Report\\{version}')

        report_path = f'..\\Report\\{version}\\{self.item_name}_{version}版本测试报告.html'
        with open(report_path, 'w', encoding='utf-8') as file:
            file.write(contents)
            file.close()
            print('您的报告已生成，目录为' + report_path)


if __name__ == '__main__':
    # result_info = {
    #     'version': "v2.0",
    #     'module': "login",
    #     'case_type': "ui",
    #     'case_id': "case-03",
    #     'case_desc': "1.输入账号；2.输入密码；3.输入验证码；4.点击登录按钮",
    #     'case_result': "test-error",
    #     'error_msg': "无",
    #     'error_sceenshot': "无",
    #     'uri': "https://172.16.13.183:8888/WoniuSales1.4/customer",
    #     'requests_method': "post",
    #     'parame': "username=admin",
    #     'expect': "login-pass"}
    result_info = ["v2.0","login","ui","case-03","1.输入账号；2.输入密码；3.输入验证码；4.点击登录按钮",
                   "test-error","无","无","https://172.16.13.183:8888/WoniuSales1.4/customer","post","username=admin","login-pass"]
    File_Uite().read_excel_value("../Test_data/test_info.ini", 'login')
    TestReport("report_db").write_report_db(result_info)
    # TestReport('report_db').generate_html_report('v2.0')
