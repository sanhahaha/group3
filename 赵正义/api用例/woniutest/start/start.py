import unittest

from HTMLTestRunner_cn import HTMLTestRunner

from woniutest.tool.util import FileUtil
from woniutest.test_case.test_api import Caradd

class Start:

    def start(self, path):

        suite = unittest.TestSuite()
        loader = unittest.TestLoader()
        test_class_info = FileUtil.get_txt(path)
        # print(test_class_info)
        tests = loader.loadTestsFr(Caradd)
        print(tests)
        suite.addTests(tests)

        with open('report.html', 'w') as file:
            runner = HTMLTestRunner(stream=file, verbosity=2)
            runner.run(suite)
if __name__ == '__main__':
    a=Start()
    a.start("../conf/start")