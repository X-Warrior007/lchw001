#About print a Chinese finger-guessing game by python

# 导入模块
import random
# 猜拳游戏
# # 定义一个变量记录用户的输入拳法
# player = int(input("请输入: 剪刀(0) 石头(1) 布(2):"))
# # 定义一个变量 记录电脑的拳法
# # randint(0, 2) == [0, 2]
# computer = random.randint(0, 2)
#
# print("用户输入:%d---电脑输入:%d" % (player, computer))
# # 判断胜负
# # 以用户为第一视角 -> 胜利 平局 失败
# # 用户胜利
# if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
#     print("玩家胜利!!!")
# # 判断平局
# elif player == computer:
#     print("平局")
# # 失败
# else:
#     print("不要走 决战到天亮!!!!")


# 死循环
while True:
    # 定义一个变量记录用户的输入拳法
    player = int(input("请输入: 剪刀(0) 石头(1) 布(2):"))
    # 定义一个变量 记录电脑的拳法
    # randint(0, 2) == [0, 2]
    computer = random.randint(0, 2)
    print("用户输入:%d---电脑输入:%d" % (player, computer))
    # 判断胜负
    # 以用户为第一视角 -> 胜利 平局 失败
    # 用户胜利
    if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
        print("玩家胜利!!!")
    # 判断平局
    elif player == computer:
        print("平局")
    # 失败
    else:
        print("不要走 决战到天亮!!!!")

    input("是否继续游戏? 如果继续请安回车!!")

