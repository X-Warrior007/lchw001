#About third adding of definding functions



# def my_func(a):
#     print(a)
#
# num = 10
# my_func(num)


# 第一个实例 -> a是不可变的
# a = 1
# b = a
# print(a)
# print(b)


# 第二个实例
# a = [1, 2]
# b = a
# print(a)
# print(b)
# a.append(3)
# print(a)
# print(b)


# python 小整数范围(-5, 256)
a = 1000
b = 1000
print(id(a))
print(id(b))


# 递归函数 就是函数调用自己本身
# 书写起来很简写 但是难以理解(可读性差)
# 设计一个递归函数(找规律)
# 递归必须有一个停止调用函数的条件

# def my_func():
#     my_func()
#
# my_func()

# 导入模块
# time 定时器模块
import time

# 重新获取验证码的业务逻辑 打印重新获取(xx) 配合函数完成
# def my_func(s):
#     while s > 0:
#         # 线程睡眠
#         time.sleep(1)
#         print("重新获取(%d)" % (s - 1))
#         s -= 1
#
# my_func(60)


# def my_func1(s):
#     if s > 0:
#         print("重新获取(%d)" % (s - 1))
#
# def my_func2(s):
#     if s > 0:
#         print("重新获取(%d)" % (s - 1))
#         my_func1(s - 1)
#
# def my_func3(s):
#     if s > 0:
#         print("重新获取(%d)" % (s - 1))
#         my_func2(s - 1)
#
# def my_func4(s):
#     if s > 0:
#         print("重新获取(%d)" % (s - 1))
#         my_func3(s - 1)
#
#
# my_func4(1)


def my_func(s):
    # 判断自己执行自己的条件
    if s > 0:
        print("重新获取(%d)" % (s - 1))
        my_func(s - 1)

my_func(60)

# 5! = 5 * 4 * 3 * 2 * 1


# 5 * 4 * 3 * 2 * 1
def my_func1(num):
    if num > 1:
        return num * my_func2(num - 1)
    else:
        return 1

# 4 * 3 * 2 *1
def my_func2(num):
    if num > 1:
        return num * my_func3(num - 1)
    else:
        return 1

# 3 * 2 * 1
def my_func3(num):
    if num > 1:
        return num * my_func4(num - 1)
    else:
        return 1

# 2 *1
# 2 * 1
def my_func4(num):
    if num > 1:
        return num * my_func5(num - 1)
    else:
        return 1

# 1
def my_func5(num):
    if num > 1:
        pass
    else:
        return 1

# 2! = 2 *1
# print(my_func4(2))

# 3! = 3 * 2 * 1
# print(my_func3(3))

# 4! = 4 * 3 * 2 * 1
# print(my_func2(4))

# 5! = # 5 * 4 * 3 * 2 * 1
# print(my_func1(5))


def my_func(num):
    # 判断是否自己执行自己的条件
    if num > 1:
        return num * my_func(num - 1)
    else:
        return 1

print(my_func(1))

# 匿名函数 -> 藏匿名字的函数
# 函数的简写 (函数另一种的表达形式)
# 配合sort函数完成自定义排序
# 把匿名函数作为参数传递(函数中)

# 无参数无返回值
# 定义
# def my_func():
#     print("哈哈")
#
# # 执行
# my_func()
# f = lambda : print("哈哈")
# 执行
# f()
# (lambda : print("哈哈"))()

# 无参数有返回值的的函数
# def my_func():
#     return "你好"
#
# ret = my_func()
# print(ret)

# f = lambda : "你好"
# ret = f()
# print(ret)

# 有参数无返回值的函数
# def my_func(name):
#     print("姓名:%s" % name)
#
# my_func("小红")

# 匿名函数
# f = lambda name: print("姓名:%s" % name)
# f("小明")

# 有参数又返回值的函数
# def add2num(a, b):
#     return a + b
# ret = add2num(10, 11)
# print(ret)

#
# f = lambda a, b: (a + b)
# ret = f(10, 11)
# print(ret)


# 定义一个匿名函数
# 匿名函数可以作为实参传入到函数内部
# f = lambda x,y:x+y
#
# # def add2num(x, y):
# #     return x + y
# def fun(a, b, opt):
#     print("a = %d" % a)
#     print("b = %d" % b)
#     ret = opt(a, b)
#     print(ret)
#     # print("result =" % opt(a, b))
#
# fun(1, 2, f)


# 列表排序-> 自定义排序

# stus = [{"name": "zhangsan", "age": 18}, {"name": "lisi", "age": 19}, {"name": "wangwu", "age": 17}]
#
# # [{"name": "wangwu", "age": 17},{"name": "zhangsan", "age": 18}, {"name": "lisi", "age": 19}]
# stus.sort(key=lambda my_dict:my_dict["name"])
# print(stus)


# my_list = [[5, 3, 5], [1, 1, 3], [9, 1, 12]]
#
# my_list.sort(key=lambda ll:ll[2])
# print(my_list)


# 当创建一个有规律的列表可以使用列表推导式完成创建

# 定义一个列表 100个元素 0~99
# 定义一个空列表
# my_list = []
# for i in range(100):
#     my_list.append(i)
# print(my_list)

# 格式: 列表名 = [临时变量(列表的元素) for 临时变量 in range(100)]
# my_list = [i for i in range(100)]
# print(my_list)


# 定义一个列表 保存1-30之间的偶数
# my_list = []
# for i in range(1, 31):
#     if i % 2 == 0:
#         my_list.append(i)
#
# print(my_list)

# 列表推导式
# my_list = [i for i in range(1, 31) if i % 2 == 0]
# print(my_list)

# 定义一个列表 每个元素是hello 10个元素
# my_list = []
# for i in range(10):
#     my_list.append("hello%d" % i)
# print(my_list)

#
# my_list = ["hello%d" % i for i in range(10)]
# print(my_list)

# 定义一个列表 每个元素是元组
# my_list = []
# for x in range(3):
#     #循环
#     for y in range(2):
#         # 创建一个元组
#         ret = (x, y)
#         my_list.append(ret)
#
# print(my_list)

# [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
# 列表推导式
# my_list = [(x, y) for x in range(3) for y in range(2)]
# print(my_list)


# 请写出一段 Python 代码实现分组一个 list 里面的元素,比如 [1,2,3,...100]变成 [[1,2,3],[4,5,6]....]
#
# 参考答案：
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
a = [x for x in range(1,101)]
# a[x:x+3]  -> 0 3 6
# [1, 2, 3]
# ret = a[0:3]
# [4, 5, 6]
# ret = a[3:6]
# [7, 8, 9]
# ret = a[6:9]
# print(ret)

# b = [a[x:x+3] for x in range(0,len(a),3)]
# print(b)


# num 是不可变的
# def my_func(b):
#     b = b + b
#     print(b)
#
# num = 10
# my_func(num)
# print(num)

# def my_func(b):
#     b += b
#     print(b)
#
# num = 10
# my_func(num)
# print(num)
# 如果一个变量为不可变 那么b = b + b  和 b += b 结果是一样的



# 如果num是可变的 b = b + b  和num是不可变的结果一样
# def my_func(b):
#     b = b + b
#     print(b)
#
# num = [1, 2]
# my_func(num)
# print(num)


# def my_func(b):
#     # b += b
#     #等同于
#     b.extend(b)
#     print(b)
#
# num = [1, 2]
# my_func(num)
# print(num)

# 面试注意(形参是一个可变的数据类型 而且是一个缺省参数)
# def my_func(b=None):
#     b = []
#     b.append(1)
#     print(b)
# 定义一个变量名 他的值 为空值类型
# a = None
# print(type(a))
# # a = 10
# print(id(a))
# print(a)
# 无论怎么调用 打印的都是[1]
# my_func()
# my_func()
# my_func()
# my_func()


