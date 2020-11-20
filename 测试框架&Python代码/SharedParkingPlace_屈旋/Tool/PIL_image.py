#! /usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageGrab
import os


# 代码思路
# 1. 首先定义一个图像识别的类ImageMatch
# 2. 定义一个初始化方法
#   2.1 定义截取的大屏画面（简称大图）的图像对象screen，定义模板图片（简称小图）的图片对象template，并且对其初始化为None。
#   2.2 定义大图的图像数据对象screen_data，定义小图的图像数据对象template_data，并且对其初始化为None。
# 3. 定义一个像素点比对的方法compare，这个方法有两个参数p1，p2，分别代表两个像素点
#   3.1 对于像素点p1和p2对应位置的元素分别进行比较
#   3.2 如果他们全部相等，就返回代表两个像素点相等的逻辑值True
#   3.3 如果有任何一组不相等，那就返回代表两个像素点不相等的逻辑值False
# 4. 定义一个查找模板图片位置坐标的方法find_image，这个方法有一个参数target，就是模板图片的名字
#   4.1 定义一个模板图片路径变量image_path并赋值
#   4.2 利用ImageGrab模块的grab方法获取大图对象，并且对其调用convert方法，参数传入RGBA，从而获取相应格式的大图对象，最后赋值screen
#   4.3 利用Image模块的open方法获取小图对象，并且对其调用convert方法，参数传入RGBA，从而获取相应格式的小图对象，最后赋值template
#   4.4 利用图像对象的属性size来分别获取大图和小图的宽高screen_width,screen_height,template_width,template_height
#   4.5 利用图像对象的方法load方法来分别获取大图和小图的rgba数据对象（PixelAccess），并将其赋值给screen_data，template_data
#   4.6 利用双层for循环来模拟滑动的过程，这里外层循环用来表示Y轴的滑动，内层for循环用来表示X轴的滑动
#   4.7 在内层循环体中进行5个特征点的比对
#       左顶点 self.compare(self.screen_data[x, y],
#                           self.template_data[0, 0])
#       右顶点 self.compare(self.screen_data[x + template_width - 1, y],
#                           self.template_data[template_width - 1, 0])
#       左下角 self.compare(self.screen_data[x, y + template_height - 1],
#                           self.template_data[0, template_height - 1])
#       右下角 self.compare(self.screen_data[x + template_width -1, y + template_height - 1],
#                           self.template_data[template_width - 1, template_height - 1])
#       中心点 self.compare(self.screen_data[x + int(template_width / 2), y + int(template_height / 2)],
#                           self.template_data[int(template_width / 2), int(template_height / 2)])
#   4.8 当5个特征点比对全部为True时，我们去做全像素匹配，调用check_match方法
#   4.9 当5个特征点比对为False时，我们什么都不做，这就意味着继续滑动到下一个位置
#   4.10 当全像素匹配成功时，我们就去计算中心点坐标，并return这个坐标结果
#   4.11 当全像素匹配不成功时，我们也是什么都不做，这就意味着继续滑动到下一个位置
#   4.12 如果双层for循环成功走出来了，此时意味着没有找到指定模板图片，所以我们最后还需要返回-1，-1表示没找到
# 5. 定义一个全像素匹配的方法check_match，这个方法有2个参数，分别表示x， y，也就是当前左顶点坐标
#   5.1 首先利用template对象的size属性来获取小图的宽高数据template_width,template_height
#   5.2 利用双层for循环来模拟像素点滑动的过程，外层for循环代表小图的Y轴方向，内层for循环代表小图的X轴方向
#   5.3 在内层for循环中检查大图和小图对应像素点的匹配情况，如果匹配就继续滑动，如果不匹配就直接返回False
#   5.4 像素点匹配时点的比较 self.compare(self.screen_data[x + small_x, y + small_y], self.template_data[small_x, small_y])
#   5.5 如果双层for循环顺利走出来，此时意味着全像素匹配成功，应该返回True
# 6. 定义一个用于断言的方法check_exists，主要用于检查传入模板图片是否存在，这个方法有一个参数target，就是模板图片的名字
#   6.1 首先调用self.find_image方法来获取指定模板图片的坐标位置
#   6.2 检查坐标位置是否为-1，-1，是则返回False，否则则返回True。
class ImageMatch:

    def __init__(self):
        # 定义大图和小图图像对象
        self.screen = None
        self.template = None
        # 定义大图和小图图像数据对象
        self.screen_data = None
        self.template_data = None

    # 定义一个像素比对方法
    def compare(self, p1, p2):
        return p1[0] == p2[0] and p1[1] == p2[1] and p1[2] == p2[2] and p1[3] == p2[3]

    # 定义一个查找指定模板图片的坐标的方法（图像识别核心代码）
    def find_image(self, target):
        image_path = os.path.join(os.getcwd(), 'source')
        # 获取当前屏幕截屏
        self.screen = ImageGrab.grab().convert('RGBA')
        # 获取模板图片
        self.template = Image.open(os.path.join(image_path, target)).convert('RGBA')
        # 获取大图和小图的宽高
        screen_width, screen_height = self.screen.size
        template_width, template_height = self.template.size
        # 获取大图和小图的数据对象
        self.screen_data = self.screen.load()
        self.template_data = self.template.load()
        # 开始进行滑动比对
        for y in range(screen_height - template_height):
            for x in range(screen_width - template_width):
                if self.compare(self.screen_data[x, y],
                                self.template_data[0, 0]) and\
                    self.compare(self.screen_data[x + template_width - 1, y],
                                 self.template_data[template_width - 1, 0]) and\
                    self.compare(self.screen_data[x, y + template_height - 1],
                                 self.template_data[0, template_height - 1]) and\
                    self.compare(self.screen_data[x + template_width - 1, y + template_height -1],
                                 self.template_data[template_width - 1, template_height - 1]) and\
                    self.compare(self.screen_data[ x + int(template_width / 2), y + int(template_height / 2)],
                                 self.template_data[int(template_width / 2), int(template_height / 2)]):
                    is_matched = self.check_match(x, y)
                    if is_matched:
                        pos_x = x + int(template_width / 2)
                        pos_y = y + int(template_height / 2)
                        return pos_x, pos_y
        return -1, -1

    # 定义一个全像素匹配的方法
    def check_match(self, x, y):
        # 获取小图的宽高
        template_width, template_height = self.template.size
        # 在小图上滑动比对
        for small_y in range(template_height):
            for small_x in range(template_width):
                if not self.compare(self.screen_data[x + small_x, y + small_y],
                                    self.template_data[small_x, small_y]):
                    return False
        return True

    # 加入了像素占比的匹配度概念的全像素匹配方法
    def check_match_plus(self, x, y, similarity=1.0):
        template_width, template_height = self.template.size
        # 计算小图像素点的个数
        total = template_width * template_height
        # 定义不匹配像素点计数器
        no_match_count = 0
        for small_y in range(template_height):
            for small_x in range(template_width):
                if not self.compare(self.screen_data[x + small_x, y + small_y],
                                    self.template_data[small_x, small_y]):
                    # 不匹配像素点统计
                    no_match_count += 1
        # 这对不匹配度进行一个比较判断
        return no_match_count / total <= 1 - similarity

    # 定义一个检查指定模板图片是否存在的方法
    def check_exists(self, target):
        x, y = self.find_image(target)
        return x != -1 and y != -1
        # if x != -1 and y != -1:
        #     return True
        # else:
        #     return False


if __name__ == '__main__':
    x, y = ImageMatch().find_image('python.png')
    print(x, y)
