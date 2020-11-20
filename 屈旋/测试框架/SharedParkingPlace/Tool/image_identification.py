import cv2
import os
import time
from PIL import ImageGrab

from pymouse import PyMouse
from pykeyboard import PyKeyboard
from FrameDemo.SharedParkingPlace.Tool.file_uite import logutil
from FrameDemo.SharedParkingPlace.Tool.file_uite import File_Uite


class ImageMatchByCV:
    
    logger = logutil.get_logger(os.path.join(os.getcwd(), 'gui_util'))
    mouse = PyMouse()
    keyboard = PyKeyboard()

    def find_image(self,target):
        # image_path = os.path.join(os.getcwd(),'image') # 定义截图保存位置
        image_path = '..\\Image'
        scree_path = os.path.join(image_path,'screen.png')
        ImageGrab.grab().save(scree_path) # 分别获取小图和大图的图像对象

        # 读取大图对象
        screen = cv2.imread(scree_path)
        # 读取小图对象
        template = cv2.imread(os.path.join(image_path, target))
        # 进行模板匹配，参数包括大图对象、小图对象和匹配算法
        result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        # 获取匹配结果
        min, max, min_loc, max_loc = cv2.minMaxLoc(result)

        similarity = File_Uite.get_ini_value('..\\Test_data\\base.ini', 'other', 'similarity')

        if max < float(similarity):
            return -1 ,-1

        x = max_loc[0] + int(template.shape[1] / 2)
        y = max_loc[1] + int(template.shape[0] / 2)
        return x, y

    @classmethod
    def click_image(cls, target):
        """
        单击一张图片
        :param target:
        :return:
        """
        x, y = cls.find_image(target)
        if x == -1 and y == -1:
            cls.logger.error(f'{target}图片未匹配')
            return
        cls.mouse.click(x, y)

    @classmethod
    def double_click_image(cls, target):
        x, y = cls.find_image(target)
        if x == -1 and y == -1:
            cls.logger.error(f'{target}图片未匹配')
            return
        cls.mouse.click(x, y, n=2)

    @classmethod
    def input_image(cls, target, msg):
        x, y = cls.find_image(target)
        if x == -1 and y == -1:
            cls.logger.error(f'{target}图片未匹配')
            return
        cls.keyboard.type_string(msg)

    @classmethod
    def select_image(cls, target, count):
        # 点击这个下拉框
        cls.click_image(target)
        # count次执行向下键
        for i in range(count):
            cls.keyboard.press_key(cls.keyboard.down_key)
        # 回车
        cls.keyboard.press_key(cls.keyboard.enter_key)

    @classmethod
    def screen_shot(cls, driver, path):
        driver.get_screenshot_as_file(path)


class Assert:

    @classmethod
    def assert_equal(cls, expect, actual):
        if expect == actual:
            test_result = 'test-pass'
        else:
            test_result = 'test-fail'
        print(test_result)


if __name__ == '__main__':
    print(ImageMatchByCV().find_image('..\\Image\\screen.png'))