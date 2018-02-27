#About using of list
# 列表的定义 有序的 可以承载各种数据(变量)类型
# 格式: 列表名 = [元素1, 元素2, 元素n]
# my_list = [1, 3.14, "hello", True]
# print(my_list)

# 定义一个空的列表
# my_list1 = []
# <class 'list'>
# print(type(my_list1))
# my_list2 = list()
# 如果看是否是一个空列表呢?
# l = len(my_list2)
# print(l)

# 定义一个列表
# my_list = ["a", "b", "c", "d"]
my_list = list("abcde")
# print(my_list)

# for循环
# for value in my_list:
#     print(value)

# while循环
# 定义一个变量 记录列表中的下标索引
# i = 0
# while i < len(my_list):
#     # 通过下标获取对应的元素
#     value = my_list[i]
#     print(value)
#     i += 1

# 列表添加元素("增"append, extend, insert)
# 定义一个列表 -> 列表是可变的
my_list = [1, 2, 3]

# append -> 追加
# my_list.append([2, 4, 6])
# print(my_list)

# extend, 可迭代对象
# my_list.extend("abcd")
# print(my_list)


# insert
# my_list.insert(100, [1, 2])
# print(my_list)

# 列表越界
# value = my_list[20]
# print(value)

# 字符串越界
# s = "abc"
# value = s[100]
# print(value)

