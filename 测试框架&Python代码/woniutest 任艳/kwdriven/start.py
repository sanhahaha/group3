from woniutestV1.tools.util import FileUtil
from woniutestV1.kwdriven.collection import Collection

class Start:

    def run(self):
        # 获取关键字方法所在的类的对象,一会要用collerction去调用
        co = Collection
        # 获取关键字配置文件内容，返回字典
        kw_map = FileUtil.get_json('intepret')

        test_script_path = FileUtil.get_txt_line('script.conf')
        for script_path in test_script_path:
            scripts = FileUtil.get_txt_line(script_path)
            for step in scripts:
                temp = step.split(',')
                # 获取关键字
                keyword = temp[0]
                params = tuple(temp[1:])
                if hasattr(co, kw_map[keyword]):
                    fun = getattr(co, kw_map[keyword])
                    fun(*params)

if __name__ == '__main__':
    Start().run()