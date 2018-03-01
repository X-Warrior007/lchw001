#About adding for the list


# 定义一个列表
# my_list = [1, 2, 3, 4, 2, 3, 2]

# 双击666
# my_list[2] = "双击666"
# print(my_list)


# <3>查找元素("查"in, not in, index, count)

# in
# if 2 in my_list:
#     print("存在")

# not in
# if 22 not in my_list:
#     print("不存在")

# index 查询元素在其列表的下标索引
# index = my_list.index(22)
# print(index)

# count 查询列表中某个元素的出现的次数
# count = my_list.count(22)
# print(count)

# 造成程序崩溃 -> 上线后 必须避免
# 如果这个元素存在 告知位置
# 如果不存在 告知就是不存在

# 解决方案01:
# if 2 in my_list:
#     index = my_list.index(2)
#     print(index)
# else:
#     print("不存在")


my_list = [1, 2, 3, 4, 2, 3, 2]

# 解决方案02
# python中 非零即真 零则假
# if my_list.count(2):
#     print("存在")
#     index = my_list.index(2)
#     print(index)
# else:
#     print("22不存在")


# 分析龟叔是如何做到的
# 定义一个变量记录下标
# i = 0
# while i < len(my_list):
#     # 对应的value
#     value = my_list[i]
#     if value == 2:
#         print(i)
#         break
#     i += 1

my_list = [1, 2, 3, 4]

# del 内置函数
# 格式: del 列表名[下标索引]
# del my_list[2]
# print(my_list)

# pop 默认会删除最后一个
# pop(下标索引) 而且有返回值的
# x = my_list.pop(1)
# print(x)
# print(my_list)

# remove
# my_list.remove(3)
# print(my_list)

# clear 清空列表
# my_list.clear()
# my_list = []

# print(my_list)

import random
# 我要定义一个列表 里面有10个元素
# 每个元素int类型 元素的大小[0, 200]之间

# 定义一个空列表
my_list = []
for i in range(10):
    value = random.randint(0,200)
    # 添加value到列表中
    my_list.append(value)

print(my_list)
# sort排序 -> 升序(数字从小到大)
# sort(reverse=False) == sort()
# my_list.sort()
# print(my_list)

# 降序(数字是从大到小)
# my_list.sort(reverse=False)
# print(my_list)

# 逆序 -> 字符串中[::-1]
# new_list = reversed(my_list)
# print(list(new_list))

schoolNames = [['北京大学', '清华大学'], ['南开大学', '天津大学', '天津师范大学'], ['山东大学', '中国海洋大学', "蓝翔大学"]]
# # 蓝翔大学
# my_list = schoolNames[2]
# # 获取大学['山东大学', '中国海洋大学', '蓝翔大学']
# name = my_list[2]
# print(name)

# 开发中常用的格式
# name = schoolNames[2][2][2]
# print(name)

# 一个学校，有3个办公室，现在有8位老师等待工位的分配，请编写程序，完成随机的分配

# [[], [], []]

# []
# [AEFCD]
# [BGH]
# ABCDEFGH
import random
# 定义一个列表保存老师
school = [[], [], []]

# 叫八位老师站好 等待分配
teacher_list = list("ABCDEFGH")
print(teacher_list)

# 遍历teacher_list
for name in teacher_list:
    # 产生随机索引
    index = random.randint(0,2)
    school[index].append(name)
    # 随机分配办公室

print(school)
