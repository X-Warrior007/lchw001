
# 字符串 "" '' """"""
# 列表 []
# 元组 ()

# 定义一个元组
# my_tuple = (1, 3.14, True, "HELLO")
# print(my_tuple)


# 定义一个空的元组
# my_tuple = ()
# <class 'tuple'>
# print(type(my_tuple))
# my_tuple = tuple()
# print(type(my_tuple))

# 特例
# 如果元组中有且只有一个元素 格式: (元素,)
# my_tuple = (1,)
# print(type(my_tuple))


my_tuple = (1, 3.14, True, "HELLO")
# 元组和列表相似
# <1>访问元组
# value = my_tuple[3]
# print(value)

# <2>修改元组 -> 元组是不可变的 不能对他进行修改 或者删除元素
# my_tuple[1] = "哈哈"


# <3>count, index
# count = my_tuple.count(1)
# print(count)

# index = my_tuple.index(3.141)
# print(index)

# if 3.141 in my_tuple:
#     index = my_tuple.index(3.141)


# 为什么有元组这个数据类型 -> 数据安全问题
# 可以认为是一个常量
# my_list = (1, 2, "3.14", 666)

# 字典的定义

# 定义一个字典
# "name" -> key (键值)
# "老王" -> value (实值)
# "name": "老王" -> key:value - > 键值对 -> 元素
# 字典中的key是不能重复的 是唯一
# 字典是无序的 (通过是否可以通过下标获取元素)
# my_dict = {"name": "老王", "age": 20, "no": "007", "name": "老李"}
# print(my_dict)
# value可以是任意类型
#但是key 必须是不可变的
# my_dict = {(1, 2, 3): "老王", "age": 20, "no": "007"}
# print(my_dict)

# 定义一个空的字典
# my_dict1 = {}
# <class 'dict'>
# print(type(my_dict1))
# my_dict2 = dict()
# print(type(my_dict2))


# my_dict = {"name": "老王", "age": 20, "no": "007"}
# 字典是无序
# 通过key获取value
# 获取007
# 格式: 字典名[key]
# value = my_dict["no"]
# print(value)

# 关于字典的key的选择 一般key都是字符串
my_dict = {"name": "老王", "age": 20, "no": "007", "info": {"a": "a", "b": "b"}}

# 如果我们获取到 "b"
# info_dict = my_dict["info"]
# # {'a': 'a', 'b': 'b'}
# print(info_dict)
# value = info_dict["b"]
# print(value)

# value = my_dict["info"]["b"]
# print(value)

# 定义一个列表
my_list = [{"name": "老王", "age": 20}, {"info": {"a": "a", "b": "b"}}, {"name": "老王", "age": 20, "no": "007", "info": {"a": "a", "b": "b"}}]
# 获取最外层的字典
# {'name': '老王', 'age': 20, 'no': '007', 'info': {'a': 'a', 'b': 'b'}}
# {'a': 'a', 'b': 'b'}
# my_dict = my_list[2]
# last_dict = my_dict["info"]
# value = last_dict["a"]
# print(value)

# value = my_list[2]["info"]["a"]
# print(value)


my_dict = {"name": "老王", "age": 20, "no": "007"}

# <1>len() 计算元素数
# l = len(my_dict)
# print(l)

# <2>keys
# keys_list = my_dict.keys()
# print(list(keys_list))


# <3>values
# values_list = my_dict.values()
# print(list(values_list))

# <4>items
# items_list = my_dict.items()
# # [('name', '老王'), ('age', 20), ('no', '007')]
# print(list(items_list))
# # 如果我想获取 20
# print(list(items_list)[1][1])

my_dict = {"name": "老王", "age": 20, "no": "007"}

# 判断name是否存在
# if "name" in my_dict:
#     print("存在")
#     my_dict["name"]


# setdefault
# None 是一个空类型代表没有值 没有返回值
# 如果使用setdefault(key)
# 如果地点中存在这个key 将把对应的value返回
# 如果没有这个key 将返回None

# 如果setdefault(key, 默认值)
# 如果key存在将把对应的value返回
# 如果key不存在 将把默认值返回 且 会吧这个key和value组成一个新的键值对添加到字典中
# ret = my_dict.setdefault("name1", "小样")
# print(my_dict)
# print(ret)


# get
# 如果使用get(key)
# 如果地点中存在这个key 将把对应的value返回
# 如果没有这个key 将返回None

# 如果get(key, 默认值)
# 如果key存在将把对应的value返回
# 如果key不存在 将把默认值返回 字典不会发生改变
value = my_dict.get("name1", "大洋")
print(my_dict)
print(value)


# 字典的遍历

# 字符串的遍历
# for c in "name":
#     print(c)

# 列表的遍历
# for value in [1, 3, 5, 7]:
#     print(value)

# 元组
# for value in (1, 4, 7, 2, 8):
#     print(value)

my_dict = {"name": "老王", "age": 20, "no": "007"}
# <1> 遍历字典的key（键）
# for key in my_dict.keys():
#     print(key)

# <2> 遍历字典的value（值）
# for value in my_dict.values():
#     print(value)

# <3> 遍历字典的项（元素）
# for items in my_dict.items():
#     print(items)

# <4> 遍历键值对
# for k, v in my_dict.items():
#     print(k, "====", v)

# str1 = "xxx"
# str2 = "www"
# # xxx www
# print(str1, str2)

# 列表下标索引
# my_list = ["老张", "老王", "老李"]
# # enumerate 通过for循环遍历列表 可以得到对应元素的下标
# for i, name in enumerate(my_list):
#     print(i, "++", name)

# 集合的定义
# 集合是无序的 集合中的元素是不能重复的
# 去重操作
# my_set = {1, 3, 5, 7, 9, 1, 3}
# # <class 'set'>
# print(type(my_set))
# print(my_set)

# 定义一个空的集合
# 他是一个字典
# my_set = {}
# my_set = set()
# print(type(my_set))


# my_set = {1, 3, 5, 7}

# 添加元素(add，update)
# add
# my_set.add(1)
# print(my_set)

# update
# my_set.update("abcd")
# print(my_set)

my_set = {1, 3, 5, 7}
# 删除元素(remove，pop，discard)
# remove
# my_set.remove(33)
# print(my_set)

# pop 因为集合是无序的 使用pop是随机删除一个元素
# my_set.pop()
# print(my_set)

# discard 如果这个元素存在 将删除 如果没有 将什么也不会走
# my_set.discard(33)
# print(my_set)

# 交集和并集( & 和 | ) -> 开发常用到的

# 定义两个集合
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# 交集 {3, 4}
# ret1 = set1 & set2
# print(ret1)

# 并集
# ret2 = set1 | set2
# print(ret2)


# 去重的功能
#
# my_list = [1, 3, 4, 3, 4, 5, 6]
# # [1, 3, 4, 5, 6]
# my_set = set(my_list)
# new_list = list(my_set)
# print(new_list)


# my_list1 = [1, 2, 3, 4]
#
# my_list2 = [3, 4, 5]



# name = "小明"
# age = 20
# # 姓名:小明,年龄:20
# # print("姓名:%s,年龄:%d" % (name, age))
# ret = "姓名:" + name + ",年龄:" + str(age)
#
# ret2 = "姓名:%s,年龄:%d" % (name, age)
# print(ret)


