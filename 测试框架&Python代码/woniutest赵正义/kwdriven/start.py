from woniutest.tool.util import FileUtil
from woniutest.kwdriven.collection import Collection
from selenium import webdriver
class Start:

    def run(self):
        # 获取关键字方法所在的类的对象
        co = Collection
        # 获取关键字配置文件内容，返回字典
        kw_map = FileUtil.get_json('../conf/intepret')
        # print(kw_map)
        test_script_path = FileUtil.get_txt_line('../conf/script.conf')

        for script_path in test_script_path:
            scripts = FileUtil.get_txt_line(script_path)
            for step in scripts:
                temp = step.split(',')
                # 获取关键字
                keyword = temp[0]
                print(temp)
                params = tuple(temp[1:])
                if hasattr(co, kw_map[keyword]):
                    # pass
                    fun = getattr(co, kw_map[keyword])
                    print(params)
                    fun(*params)

if __name__ == '__main__':
    Start().run()
    # webdriver.Edge()