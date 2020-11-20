import unittest
from FrameDemo.SharedParkingPlace.Action.do_store import Dostore
from FrameDemo.SharedParkingPlace.Tool.file_uite import File_Uite
from FrameDemo.SharedParkingPlace.Tool.gui_util import uiutil
from FrameDemo.SharedParkingPlace.Action.do_login import login
from FrameDemo.SharedParkingPlace.Test.test_report import TestReport
from FrameDemo.SharedParkingPlace.Kw_driver.ddt_collection import Collection

class Test_store:

    def start_condtion_query(self):
        driver = uiutil.get_driver()
        login(driver).do_login('admin', 'Milor123', '0000')
        Dostore().click_store()
        Dostore().input_art()
        Dostore().click_condtion_query()
        attr = str(uiutil().find_element('store', 'store_button'))
        Collection().assert_exist_element(attr) # 断言


    def write_report(self):
        result = File_Uite.get_txt('../Test_data/result/result.txt') # 根据结果生成报告
        result_list = []
        error_msg_list = []
        sceenshot_list = []
        if result in '页面存在该元素，测试成功':
            result_list.append('测试通过')
        else:
            result_list.append('测试不通过')

        list1 = File_Uite().read_excel_value("../Test_data/test_info.ini", 'login')

        result_info = [list1[0]['version'],
                       list1[0]['module'],
                       list1[0]['type'],
                       list1[0]['caseid'],
                       list1[0]['desc'],
                       result_list,
                       error_msg_list,
                       sceenshot_list,
                       list1[0]['uri'],
                       list1[0]['remethod'],
                       list1[0]['username'] + list1[0]['password'] + list1[0]['verifycode'],
                       list1[0]['expect'],
                       ]
        TestReport("report_db").write_report_db(result_info)
        TestReport('report_db').generate_html_report('v2.0')
