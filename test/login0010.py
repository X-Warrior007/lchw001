#About print the ID card

import random
# 编程实现对一个元素全为数字的列表，求最大值、最小值
# 随机生成一个 8个元素 -100,100

# 定义一个空的列表
my_list = []
for value in range(8):
    my_list.append(random.randint(-100, 0))

print(my_list)

# 最大值
# 定义一个变量保存最大值
# my_max = my_list[0]
# # 遍历
# for value in my_list:
#     # 使用if 判断value 还是my_max大
#     if value > my_max:
#         my_max = value
#
# print("最大值:%d" % my_max)

# 比如："hello world" 字符串统计的结果为： h:1 e:1 l:3 o:2 d:1 r:1 w:1

a = "hello world"
# count = a.count("l")
# print(count)

# 方案01
# 定义一个列表

# my_list = []
# # 遍历字符串
# for c in a:
#     # 通过遍历的每个字符串计算每个字符串在字符串中个数
#     # 如果不是空格 在计算
#     if c != " " and c not in my_list:
#         count = a.count(c)
#         print("%s:%d" % (c, count))
#         my_list.append(c)


# 方案02
# 定义一个集合
my_set = set(a)
# print(my_set)

# 遍历集合
for value in my_set:
    # 如果不是空格
    if value != " ":
        count = a.count(value)
        print("%s:%d" % (value, count))


# 保存学生数据
# 小明 20
# 小红 22
# [{"name": "小明", "age": 20},{"name": "小红", "age": 22}]
# for dict in list:
#     if "小明" in dict:
#         删除
#     else:
#         print("输入的姓名有误")


# all_dict = {"小明": {"name": "小明", "age": 20}, "小红": {"name": "小红", "age": 22}}
#
# if "小明" in all_dict:
#     删除
# else:
#     有误



# 定义一个字符串
str_info = """请选择:
1.添加名片
2.删除名片
3.修改名片
4.查询名片
5.退出系统
"""
# 定义一个字典保存所有人的数据
all_dict = {}

# 死循环
while True:
    index = input(str_info)
    # 进行判断
    if index.isdigit() and (0 < int(index) < 6):
        # 1.添加名片
        if index == "1":
            my_name = input("请输入您的名字:")
            my_age = input("请输入您的年龄:")
            # 定义一个字典保存个人数据
            my_dict = {"name": my_name, "age": my_age}
            # 保存到大字典中
            all_dict[my_name] = my_dict
            print("保存数据成功...")
        # 2.删除名片
        elif index == "2":
            my_name = input("请输入删除的名字:")
            # 判断
            if my_name in all_dict:
                # 删除
                del all_dict[my_name]
                print("删除数据成功...")
            else:
                print("您输入的名字有误!!!")
        # 3.修改名片
        elif index == "3":
            my_name = input("请输入删除的名字:")
            # 判断
            if my_name in all_dict:
                my_age = input("请输入修改的年龄:")
                all_dict[my_name]["age"] = my_age
                print("修改数据完成...")
            else:
                print("您输入的名字有误!!!")
        # 4.查询名片
        elif index == "4":
            my_name = input("请输入删除的名字:")
            # 判断
            if my_name in all_dict:
                print(all_dict[my_name])
            else:
                print("您输入的名字有误!!!")
        # 5.退出系统
        elif index == "5":
            print("欢迎下次使用!")
            break
    else:
        print("输入有误")

# 保存学生数据
# 小明 20
# 小红 22
# [{"name": "小明", "age": 20},{"name": "小红", "age": 22}]
# for dict in list:
#     if "小明" in dict:
#         删除
#     else:
#         print("输入的姓名有误")


# all_dict = {"小明": {"name": "小明", "age": 20}, "小红": {"name": "小红", "age": 22}}
#
# if "小明" in all_dict:
#     删除
# else:
#     有误



# 定义一个字符串
str_info = """请选择:
1.添加名片
2.删除名片
3.修改名片
4.查询名片
5.退出系统
"""
# 定义一个字典保存所有人的数据
all_dict = {}

# 死循环
while True:
    index = input(str_info)
    # 进行判断
    if index.isdigit() and (0 < int(index) < 6):
        # 1.添加名片
        if index == "1":
            my_name = input("请输入您的名字:")
            my_age = input("请输入您的年龄:")
            # 定义一个字典保存个人数据
            my_dict = {"name": my_name, "age": my_age}
            # 保存到大字典中
            all_dict[my_name] = my_dict
            print("保存数据成功...")
        # 2.删除名片
        elif index == "2":
            my_name = input("请输入删除的名字:")
            # 判断
            if my_name in all_dict:
                # 删除
                del all_dict[my_name]
                print("删除数据成功...")
            else:
                print("您输入的名字有误!!!")
        # 3.修改名片
        elif index == "3":
            my_name = input("请输入删除的名字:")
            # 判断
            if my_name in all_dict:
                my_age = input("请输入修改的年龄:")
                all_dict[my_name]["age"] = my_age
                print("修改数据完成...")
            else:
                print("您输入的名字有误!!!")
        # 4.查询名片
        elif index == "4":
            my_name = input("请输入删除的名字:")
            # 判断
            if my_name in all_dict:
                print(all_dict[my_name])
            else:
                print("您输入的名字有误!!!")
        # 5.退出系统
        elif index == "5":
            print("欢迎下次使用!")
            break
    else:
        print("输入有误")


