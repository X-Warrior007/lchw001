#About second adding of the Airplane Games

# 导入模块
# import pygame
# import sys

import pygame, sys

# pygame进行实例化
pygame.init()

# 创建游戏窗口-> 返回一个游戏窗口对象
# set_mode([400, 400]) -> (列表)[游戏窗口的宽度, 游戏窗口的高度]
# 单位是像素
window = pygame.display.set_mode([512, 768])

# 设置游戏窗口的标题
pygame.display.set_caption("飞机大战")

# 加载本地资源图片 返回一个图片对象
logo_image = pygame.image.load("res/app.ico")
# 设置游戏窗口的logo
pygame.display.set_icon(logo_image)

# 游戏背景图片对象添加到游戏窗口中
# 加载本地资源图片 返回一个游戏背景图片对象
bg_image = pygame.image.load("res/img_bg_level_1.jpg")


# 加载本地资源图片 返回一个英雄飞机图片对象
hero_image = pygame.image.load("res/hero2.png")

# 定义一个变量 记录x轴
my_x = 0

# 死循环 在死循环中监听无论鼠标点击事件 或者键盘按键的事件
while True:
    # 图片添加到窗口中
    # blit(添加到游戏窗口中图片对象, (0, 0)) (x, y) 坐标
    window.blit(bg_image, (0, 0))
    # 添加飞机
    window.blit(hero_image, (my_x, 0))
    # 记得刷新游戏窗口
    pygame.display.update()
    my_x += 3
    # 获取所有游戏窗口的中的事件监听-> 列表
    event_list = pygame.event.get()
    # 遍历所有的事件
    for event in event_list:
        # 判断如果是鼠标点击了
        if event.type == pygame.QUIT:
            # 退出游戏
            # 停止pygame 游戏引擎
            pygame.quit()
            # 退出程序
            sys.exit()

        # 监听esc键按下
        if event.type == pygame.KEYDOWN:
            # 判断是否按得是esc
            if event.key == pygame.K_ESCAPE:
                # 退出游戏
                # 停止pygame 游戏引擎
                pygame.quit()
                # 退出程序
                sys.exit()

    # 监听键盘中的按键长按-> 元组(只有两种情况 0 或者 1) -> ASCII
    pressed_keys = pygame.key.get_pressed()
    # 判断向上的按键是否在长按(1)
    if pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]:
        print("向上")

    # 判断向下的按键是否在长按(1)
    if pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]:
        print("向下")

    # 判断向左的按键是否在长按(1)
    if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
        print("向左")

    # 判断向右的按键是否在长按(1)
    if pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
        print("向右")

# 导入模块
# import pygame
# import sys

import pygame, sys

# pygame进行实例化
pygame.init()

# 创建游戏窗口-> 返回一个游戏窗口对象
# set_mode([400, 400]) -> (列表)[游戏窗口的宽度, 游戏窗口的高度]
# 单位是像素
window = pygame.display.set_mode([512, 768])

# 设置游戏窗口的标题
pygame.display.set_caption("飞机大战")

# 加载本地资源图片 返回一个图片对象
logo_image = pygame.image.load("res/app.ico")
# 设置游戏窗口的logo
pygame.display.set_icon(logo_image)

# 游戏背景图片对象添加到游戏窗口中
# 加载本地资源图片 返回一个游戏背景图片对象
bg_image = pygame.image.load("res/img_bg_level_1.jpg")

# 加载本地资源图片 返回一个英雄飞机图片对象
hero_image = pygame.image.load("res/hero2.png")
# 获取英雄飞机图片矩形
hero_image_rect = hero_image.get_rect()
# <rect(0, 0, 120, 78)> -> 元组(x, y, w, h)
print(hero_image_rect)

def event():
    # 获取所有游戏窗口的中的事件监听-> 列表
    event_list = pygame.event.get()
    # 遍历所有的事件
    for event in event_list:
        # 判断如果是鼠标点击了
        if event.type == pygame.QUIT:
            # 退出游戏
            # 停止pygame 游戏引擎
            pygame.quit()
            # 退出程序
            sys.exit()

        # 监听esc键按下
        if event.type == pygame.KEYDOWN:
            # 判断是否按得是esc
            if event.key == pygame.K_ESCAPE:
                # 退出游戏
                # 停止pygame 游戏引擎
                pygame.quit()
                # 退出程序
                sys.exit()

    # 监听键盘中的按键长按-> 元组(只有两种情况 0 或者 1) -> ASCII
    pressed_keys = pygame.key.get_pressed()
    # 判断向上的按键是否在长按(1)
    if pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]:
        print("向上")

    # 判断向下的按键是否在长按(1)
    if pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]:
        print("向下")

    # 判断向左的按键是否在长按(1)
    if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
        print("向左")

    # 判断向右的按键是否在长按(1)
    if pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
        print("向右")

# 死循环 在死循环中监听无论鼠标点击事件 或者键盘按键的事件
while True:
    # 图片添加到窗口中
    # blit(添加到游戏窗口中图片对象, (0, 0)) (x, y) 坐标
    window.blit(bg_image, (0, 0))
    # 添加飞机
    window.blit(hero_image, (hero_image_rect[0], hero_image_rect[1]))
    # 记得刷新游戏窗口
    pygame.display.update()
    # 改变图片的位置(相对于当前的图片位置)
    hero_image_rect.move_ip(3, 3)

    event()


import pygame, sys

# 自定义一个游戏窗口管理类
class GameWindow(object):

    # 构造方法
    def __init__(self):
        # pygame进行实例化
        pygame.init()
        # 创建游戏窗口-> 返回一个游戏窗口对象
        self.window = pygame.display.set_mode([512, 768])
        # 设置游戏窗口的标题
        pygame.display.set_caption("飞机大战")
        # 加载本地资源图片 返回一个图片对象
        logo_image = pygame.image.load("res/app.ico")
        # 设置游戏窗口的logo
        pygame.display.set_icon(logo_image)

    # 运行游戏程序
    def run(self):
        while True:
            self.__action()
            self.__draw()
            self.__event()
            self.__update()

    # 1.处理各种矩形坐标移动
    def __action(self):
        pass

    # 2.根据矩形坐标，重新对元素进行绘制
    def __draw(self):
        pass

    # 3.处理窗口中的监听事件
    def __event(self):
        # 获取所有游戏窗口的中的事件监听-> 列表
        event_list = pygame.event.get()
        # 遍历所有的事件
        for event in event_list:
            # 判断如果是鼠标点击了
            if event.type == pygame.QUIT:
                self.game_over()

            # 监听esc键按下
            if event.type == pygame.KEYDOWN:
                # 判断是否按得是esc
                if event.key == pygame.K_ESCAPE:
                    self.game_over()

                # 判断是佛按得是空格
                if event.key == pygame.K_SPACE:
                    print("发射子弹")

        # 监听键盘中的按键长按-> 元组(只有两种情况 0 或者 1) -> ASCII
        pressed_keys = pygame.key.get_pressed()
        # 判断向上的按键是否在长按(1)
        if pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]:
            print("向上")

        # 判断向下的按键是否在长按(1)
        if pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]:
            print("向下")

        # 判断向左的按键是否在长按(1)
        if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
            print("向左")

        # 判断向右的按键是否在长按(1)
        if pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
            print("向右")

    # 4.刷新窗口
    def __update(self):
        pass

    # 结束游戏
    def game_over(self):
        # 退出游戏
        # 停止pygame 游戏引擎
        pygame.quit()
        # 退出程序
        sys.exit()


# 主函数
def main():
    # 创建一个游戏窗口对象
    game_window = GameWindow()
    # 执行游戏
    game_window.run()



if __name__ == '__main__':
    main()


import pygame, sys, random

# 定义一个常量(赋值后不能修改)常量一般使用大写字母
WINDOW_WIDTH, WINDOW_HEIGHT = 512, 768
# python中 崇尚的是一切靠自觉

# 自定义一个地图类
class GameMap(object):

    def __init__(self):
        self.num = str(random.randint(1, 5))
        # 图片
        self.img_1 = pygame.image.load("res/img_bg_level_" + self.num + ".jpg")
        self.img_2 = pygame.image.load("res/img_bg_level_" + self.num + ".jpg")
        # 设置和记录图片的y轴
        self.img1_y = -WINDOW_HEIGHT
        self.img2_y = 0
        # 速度
        self.speed = 2

    # 向下移动
    def move_down(self):

        # 地图的y轴重置
        if self.img1_y >= 0:
            self.img1_y = -WINDOW_HEIGHT
            self.img2_y = 0

        self.img1_y += self.speed
        self.img2_y += self.speed






# 自定义一个游戏窗口管理类
class GameWindow(object):

    # 构造方法
    def __init__(self):
        # pygame进行实例化
        pygame.init()
        # 创建游戏窗口-> 返回一个游戏窗口对象
        self.window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
        # 设置游戏窗口的标题
        pygame.display.set_caption("飞机大战")
        # 加载本地资源图片 返回一个图片对象
        logo_image = pygame.image.load("res/app.ico")
        # 设置游戏窗口的logo
        pygame.display.set_icon(logo_image)

        # 地图对象
        self.map = GameMap()


    # 运行游戏程序
    def run(self):
        while True:
            self.__action()
            self.__draw()
            self.__event()
            self.__update()

    # 1.处理各种矩形坐标移动
    def __action(self):
        # 地图动画
        self.map.move_down()

    # 2.根据矩形坐标，重新对元素进行绘制
    def __draw(self):
        # 添加地图图片
        self.window.blit(self.map.img_1, (0, self.map.img1_y))
        self.window.blit(self.map.img_2, (0, self.map.img2_y))

    # 3.处理窗口中的监听事件
    def __event(self):
        # 获取所有游戏窗口的中的事件监听-> 列表
        event_list = pygame.event.get()
        # 遍历所有的事件
        for event in event_list:
            # 判断如果是鼠标点击了
            if event.type == pygame.QUIT:
                self.game_over()

            # 监听esc键按下
            if event.type == pygame.KEYDOWN:
                # 判断是否按得是esc
                if event.key == pygame.K_ESCAPE:
                    self.game_over()

                # 判断是佛按得是空格
                if event.key == pygame.K_SPACE:
                    print("发射子弹")

        # 监听键盘中的按键长按-> 元组(只有两种情况 0 或者 1) -> ASCII
        pressed_keys = pygame.key.get_pressed()
        # 判断向上的按键是否在长按(1)
        if pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]:
            print("向上")

        # 判断向下的按键是否在长按(1)
        if pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]:
            print("向下")

        # 判断向左的按键是否在长按(1)
        if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
            print("向左")

        # 判断向右的按键是否在长按(1)
        if pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
            print("向右")

    # 4.刷新窗口
    def __update(self):
        pygame.display.update()

    # 结束游戏
    def game_over(self):
        # 退出游戏
        # 停止pygame 游戏引擎
        pygame.quit()
        # 退出程序
        sys.exit()


# 主函数
def main():
    # 创建一个游戏窗口对象
    game_window = GameWindow()
    # 执行游戏
    game_window.run()



if __name__ == '__main__':
    main()




