#About Third adding of Airplane Games

import pygame, sys, random

# 定义一个常量(赋值后不能修改)常量一般使用大写字母
WINDOW_WIDTH, WINDOW_HEIGHT = 512, 768
# python中 崇尚的是一切靠自觉

# 自定义一个英雄飞机类
class HeroPlane(object):

    def __init__(self):
        # 赋值
        self.img = pygame.image.load("res/hero2.png")
        # 获取图片矩形
        self.img_rect = self.img.get_rect()
        # 设置飞机的初始位置
        self.img_rect.move_ip((WINDOW_WIDTH - self.img_rect[2])/2, WINDOW_HEIGHT - self.img_rect[3] - 50)
        # 飞机速度
        self.speed = 3

    # 向上
    def move_up(self):
        # 边缘检测
        if self.img_rect[1] >= 0:
            self.img_rect.move_ip(0, -self.speed)

    # 向下
    def move_down(self):
        # 边缘检测
        if self.img_rect[1] <= WINDOW_HEIGHT - self.img_rect[3]:
            self.img_rect.move_ip(0, self.speed)

    # 向左
    def move_left(self):
        # 边缘检测
        if self.img_rect[0] >= 0:
            self.img_rect.move_ip(-self.speed, 0)

    # 向右
    def move_right(self):
        # 边缘检测
        if self.img_rect[0] <= WINDOW_WIDTH - self.img_rect[2]:
            self.img_rect.move_ip(self.speed, 0)

    # 发射子弹
    def shot(self):
        print("发射子弹")



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
        # 英雄飞机对象
        self.hero_plane = HeroPlane()


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
        # 飞机图片
        self.window.blit(self.hero_plane.img, (self.hero_plane.img_rect[0], self.hero_plane.img_rect[1]))

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

                # 判断是否按得是空格
                if event.key == pygame.K_SPACE:
                    self.hero_plane.shot()

        # 监听键盘中的按键长按-> 元组(只有两种情况 0 或者 1) -> ASCII
        pressed_keys = pygame.key.get_pressed()
        # 判断向上的按键是否在长按(1)
        if pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]:
            self.hero_plane.move_up()

        # 判断向下的按键是否在长按(1)
        if pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]:
            self.hero_plane.move_down()

        # 判断向左的按键是否在长按(1)
        if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
            self.hero_plane.move_left()

        # 判断向右的按键是否在长按(1)
        if pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
            self.hero_plane.move_right()

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

import pygame, sys, random

# 定义一个常量(赋值后不能修改)常量一般使用大写字母
WINDOW_WIDTH, WINDOW_HEIGHT = 512, 768
# python中 崇尚的是一切靠自觉

# 自定义一个英雄飞机子弹类
class PlaneBullet(object):

    def __init__(self):
        # 图片
        self.img = pygame.image.load("res/bullet_10.png")
        # 获取子弹的图片矩形
        self.img_rect = self.img.get_rect()
        # 子弹的状态
        self.is_shot = False
        # 速度
        self.speed = 4

    # 向上移动
    def move_up(self):
        self.img_rect.move_ip(0, -self.speed)
        # 注意改变子弹的状态
        if self.img_rect[1] <= -self.img_rect[3]:
            # 设置为未发射状态
            self.is_shot = False


# 自定义一个英雄飞机类
class HeroPlane(object):

    def __init__(self):
        # 赋值
        self.img = pygame.image.load("res/hero2.png")
        # 获取图片矩形
        self.img_rect = self.img.get_rect()
        # 设置飞机的初始位置
        self.img_rect.move_ip((WINDOW_WIDTH - self.img_rect[2])/2, WINDOW_HEIGHT - self.img_rect[3] - 50)
        # 飞机速度
        self.speed = 3
        # 子弹弹夹
        self.bullet_list = [PlaneBullet() for i in range(6)]


    # 向上
    def move_up(self):
        # 边缘检测
        if self.img_rect[1] >= 0:
            self.img_rect.move_ip(0, -self.speed)

    # 向下
    def move_down(self):
        # 边缘检测
        if self.img_rect[1] <= WINDOW_HEIGHT - self.img_rect[3]:
            self.img_rect.move_ip(0, self.speed)

    # 向左
    def move_left(self):
        # 边缘检测
        if self.img_rect[0] >= 0:
            self.img_rect.move_ip(-self.speed, 0)

    # 向右
    def move_right(self):
        # 边缘检测
        if self.img_rect[0] <= WINDOW_WIDTH - self.img_rect[2]:
            self.img_rect.move_ip(self.speed, 0)

    # 发射子弹
    def shot(self):
        # 遍历所有的子弹
        for bullet in self.bullet_list:
            # 判断未发射的
            if not bullet.is_shot:
                # 设置子弹的位置
                bullet.img_rect[0] = self.img_rect[0] + (self.img_rect[2] - bullet.img_rect[2])/2
                bullet.img_rect[1] = self.img_rect[1] - bullet.img_rect[3]

                # 设置为发射状态
                bullet.is_shot = True
                # 一次只能发射一颗子弹
                break


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
        # 英雄飞机对象
        self.hero_plane = HeroPlane()


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

        # 遍历子弹 叫子弹飞一会
        for bullet in self.hero_plane.bullet_list:
            # 判断如果已经发射
            if bullet.is_shot:
                bullet.move_up()

    # 2.根据矩形坐标，重新对元素进行绘制
    def __draw(self):
        # 添加地图图片
        self.window.blit(self.map.img_1, (0, self.map.img1_y))
        self.window.blit(self.map.img_2, (0, self.map.img2_y))
        # 飞机图片
        self.window.blit(self.hero_plane.img, (self.hero_plane.img_rect[0], self.hero_plane.img_rect[1]))
        # 添加子弹
        for bullet in self.hero_plane.bullet_list:
            # 判断如果已经发射的子弹
            if bullet.is_shot:
                self.window.blit(bullet.img, (bullet.img_rect[0], bullet.img_rect[1]))



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

                # 判断是否按得是空格
                if event.key == pygame.K_SPACE:
                    self.hero_plane.shot()

        # 监听键盘中的按键长按-> 元组(只有两种情况 0 或者 1) -> ASCII
        pressed_keys = pygame.key.get_pressed()
        # 判断向上的按键是否在长按(1)
        if pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]:
            self.hero_plane.move_up()

        # 判断向下的按键是否在长按(1)
        if pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]:
            self.hero_plane.move_down()

        # 判断向左的按键是否在长按(1)
        if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
            self.hero_plane.move_left()

        # 判断向右的按键是否在长按(1)
        if pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
            self.hero_plane.move_right()

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





