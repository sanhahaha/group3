from FrameDemo.SharedParkingPlace.Tool.file_uite import File_Uite
from FrameDemo.SharedParkingPlace.Kw_driver.ddt_collection import Collection


class Start:

    def run(self):
        # 获取关键字方法所在的类的对象
        co = Collection
        # 获取关键字配置文件内容，返回字典
        kw_map = File_Uite.read_json('kw_script/intepret')  # 数据驱动对应的操作方法名
        test_script_path = File_Uite.get_txt_line('../Config/ddt_script.conf')  # 登录数据
        for script_path in test_script_path:
            scripts = File_Uite.get_txt_line(script_path)
            for step in scripts:  # 登录数据
                temp = step.split(',')
                # 获取关键字
                keyword = temp[0]
                params = tuple(temp[1:])
                if hasattr(co, kw_map[keyword]):
                    fun = getattr(co, kw_map[keyword]) # 元素为全路径的xpath
                    fun(*params)


if __name__ == '__main__':
    obj = Start()
    obj.run()