#About the Airplane Games

# 导入pygame模块
import pygame

# 对pygame进行实例化 叫硬件做准备(例如声卡或者显卡)
pygame.init()

# 导入模块
import pygame

# pygame进行实例化
pygame.init()

# 创建游戏窗口
# set_mode([400, 400]) -> (列表)[游戏窗口的宽度, 游戏窗口的高度]
# 单位是像素
pygame.display.set_mode([400, 400])

# 设置游戏窗口的标题
pygame.display.set_caption("飞机大战")

# 加载本地资源图片 返回一个图片对象
logo_image = pygame.image.load("res/app.ico")
# 设置游戏窗口的logo
pygame.display.set_icon(logo_image)

input()

# 导入模块
# import pygame
# import sys

import pygame, sys

# pygame进行实例化
pygame.init()

# 创建游戏窗口
# set_mode([400, 400]) -> (列表)[游戏窗口的宽度, 游戏窗口的高度]
# 单位是像素
pygame.display.set_mode([400, 400])

# 设置游戏窗口的标题
pygame.display.set_caption("飞机大战")

# 加载本地资源图片 返回一个图片对象
logo_image = pygame.image.load("res/app.ico")
# 设置游戏窗口的logo
pygame.display.set_icon(logo_image)

# 死循环 在死循环中监听无论鼠标点击事件 或者键盘按键的事件
while True:
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

# 导入模块
# import pygame
# import sys

import pygame, sys

# pygame进行实例化
pygame.init()

# 创建游戏窗口
# set_mode([400, 400]) -> (列表)[游戏窗口的宽度, 游戏窗口的高度]
# 单位是像素
pygame.display.set_mode([400, 400])

# 设置游戏窗口的标题
pygame.display.set_caption("飞机大战")

# 加载本地资源图片 返回一个图片对象
logo_image = pygame.image.load("res/app.ico")
# 设置游戏窗口的logo
pygame.display.set_icon(logo_image)

# 死循环 在死循环中监听无论鼠标点击事件 或者键盘按键的事件
while True:
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



