from woniutest.test_case.test_api import Caradd
from woniutest.tool.util import FileUtil


class Start:

    def run(self):

        co = Caradd()

        test_script_path = FileUtil.get_txt_line('../conf/sariptapi.conf')

        for script_path in test_script_path:
            scripts = FileUtil.get_txt_line(script_path)
            for step in scripts:
                temp = step.split(',')
                # 获取关键字
                keyword = temp[1]
                print(temp)

                if hasattr(co,keyword):
                    getattr(co, keyword)()
if __name__ == '__main__':
    Start().run()





















