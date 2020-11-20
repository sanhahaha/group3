from FrameDemo.SharedParkingPlace.Tool.gui_util import uiutil
from FrameDemo.SharedParkingPlace.Tool.file_uite import File_Uite
from FrameDemo.SharedParkingPlace.Tool.file_uite import logutil
from FrameDemo.SharedParkingPlace.Tool.file_uite import db_Util
from FrameDemo.SharedParkingPlace.Action.do_sales import Dosales
from FrameDemo.SharedParkingPlace.Action.do_login import login
from FrameDemo.SharedParkingPlace.Action.do_customer import Customer
import os

class customer_cases:
    def __init__(self):
        self.driver = uiutil.get_driver()
        self.data = File_Uite.get_ini_section('..\\Test_data\\test_info.ini', 'customer')


    def customer_0(self,info):
        '''
        验证是否新增成功

        1 = True
        0 = False
        :return:
        '''
        logger = logutil.get_logger(
            os.path.join(
                os.getcwd(),
                info['log_info']))   # 获得日志生成器对象
        try:
            customerphone = self.data[0]['customerphone']
            customername = self.data[0]['customername']
            childsex = self.data[0]['childsex']
            childdate = self.data[0]['childdate']
            creditkids = self.data[0]['creditkids']
            creditcloth = self.data[0]['creditcloth']
            Customer().into_customer_page() # 进入会员管理页面
            Customer().add_into(customerphone,customername,creditkids,creditcloth) # 执行添加动作

            da_data = (db_Util('db_info').query_one("SELECT * FROM `customer` WHERE  customerphone=%s;"%customerphone))
            logger.info('customer_01读取正确')

            if customerphone in da_data[1]:
                print('用户新增成功，和数据库数据匹配')
                return int(1)
            else:
                print('用户新增失败，数据库数据不匹配')
                return int(0)
        except BaseException:
            logger.error('customer_01读取错误')
            return int(0)
        finally:
            print('customer_01''执行完毕')

    def customer_query_01(self):
        '''
        验证是否查询成功

        1 = True
        0 = False
        :return:
        '''
        logger = logutil.get_logger(
            os.path.join(
                os.getcwd(),
                'customer_query_01'))  # 获得日志生成器对象
        try:
            customerphone = self.data[6]['customerphone']
            # Customer().into_customer_page()  # 进入会员管理页面
            Customer().query_into(customerphone) # 执行查询动作

            da_data = (db_Util('db_report').query_one("SELECT * FROM `customer` WHERE  customerphone=%s;" % customerphone))
            print(da_data[1])
            logger.info('customer_query_01读取正确')

            if customerphone in da_data[1]:
                print('用户查询成功，和数据库数据匹配')
                return int(1)
            else:
                print('用户查询失败，数据库数据不匹配')
                return int(0)
        except BaseException:
            logger.error('customer_query_01读取错误')
            return int(0)
        finally:
            print('customer_query_01''执行完毕')

    def customer_edit_01(self):
        '''
        验证是否修改成功

        1 = True
        0 = False
        :return:
        '''
        logger = logutil.get_logger(
            os.path.join(
                os.getcwd(),
                'customer_edit_01'))  # 获得日志生成器对象
        try:
            customerphone = self.data[8]['customerphone']
            customerphones = self.data[8]['customerphones']
            # Customer().into_customer_page()  # 进入会员管理页面
            Customer().alter_into(customerphone,customerphones)  # 执行修改动作


            da_data = (db_Util('db_report').query_one("SELECT * FROM `customer` WHERE  customerphone=%s;" % customerphones))
            logger.info('customer_edit_01读取正确')

            if customerphones in da_data[1]:
                print('用户修改成功，和数据库数据匹配')
                return int(1)
            else:
                print('用户修改失败，数据库数据不匹配')
                return int(0)

        except BaseException:
            logger.error('customer_edit_01读取错误')
            return int(0)
        finally:
            self.driver.close()
            print('customer_edit_01''执行完毕')

if __name__ == '__main__':
    obj = customer_cases()
    print(obj.customer_edit_01())
