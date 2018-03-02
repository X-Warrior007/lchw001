#About the second adding of definying functions 



# 缺省参数: 定义的函数中的形参 有了默认值
# 如果在执行函数的时候 没有给有默认值的形参设置实参 那么久会使用形参的默认值
# 定义一个函数 打印名字 和年龄 小明 20 ->班级人数的80人中 80%
def print_info(name, age=20):
    print("姓名:%s" % name)
    print("年龄:%d" % age)

# 执行函数
# print_info("小明")

# print_info("小红")
# 老王 30 -> 班级人数的20人 中的20%
print_info("老王", 90)


# 定义一个函数
# def my_func(my_list):
#     print(my_list[1])
#     print(my_list[3])
#
# # 执行函数的时候 注意列表类型 -> []
# my_func([1, 3, 4, 5, 8])


# 不定长参数之元组
def my_func(*args):
    #测试
    print(type(args))
    print(args[0])

# 执行函数
my_func(1, 3, 5, 6)

# 意义: 定义函数时候少写了很多形参
# 执行函数的时候 你只要当前你的参数为元组 但是不用考虑添加()


# 不定长参数之元组
# def my_func(*args):
#     #测试
#     print(type(args))
#     print(args[0])
#
# # 执行函数 -> 遵循位置参数
# my_func(1, 3, 5, 6)


# 定义这个函数的时候
# 不定长参数之字典
# def my_func(**kwargs):
#     print(type(kwargs))
#     print(kwargs)
    # print(kwargs["name"])
    # print(kwargs["age"])
# 如果我们想执行函数 我要使用关键字参数执行

# 执行函数 -> 遵循关键字参数
# my_func(name="小明", age=20)
# 无论是不定长参数元组还是字典
# 默认情况下 如果不添加实参 那么元组和字典都有默认值 为空的元组和字典


#如果定义了一个函数 如果使用了缺省参数 那么后面的形参都要用缺省参数
# def my_func(name, no, age=20):
#     print(name)
#     print(age)


# 不定长参数元组和缺省参数是平级 位置可以互换
# 不定长参数之字典 必须在函数的尾部
# 了解 看懂 不要写
# def my_func(a, b, c=10, *args, **kwargs):
#     print(a)
#     print(b)
#     print(c)
#     print(args)
#     print(kwargs)
#
# my_func(1, 3, name="小明", age=20)


# 业务需求
# 定义一个函数 接收一个数字(分数) 返回 一个字符串(优 良 中 差)
# 如果一个函数中包含多个return 那么只要有一个执行后 后面return将不会再执行
# 而且执行完return 后面的代码也不会再执行 代表执行return标识函数执行完成
# def my_func(score):
#     # 判断
#     if score >= 90:
#         return "优"
#     elif score >= 80:
#         return "良"
#     elif score >= 60:
#         print("测试111")
#         return "中"
#         print("测试")
#     else:
#         return "差"



# 执行函数
# ret = my_func(60)
# print(ret)


# def my_func(score):
#     name = ""
#     # 判断
#     if score >= 90:
#         name = "优"
#     elif score >= 80:
#         name = "良"
#     elif score >= 60:
#         name = "中"
#     else:
#         name = "差"
#
#     return name
#
# print(my_func(60))

# 业务需求
# 定义一个函数 接收一个数字(分数) 返回 一个字符串(优 良 中 差)
# 如果一个函数中包含多个return 那么只要有一个执行后 后面return将不会再执行
# 而且执行完return 后面的代码也不会再执行 代表执行return标识函数执行完成
# def my_func(score):
#     # 判断
#     if score >= 90:
#         return "优"
#     elif score >= 80:
#         return "良"
#     elif score >= 60:
#         print("测试111")
#         return "中"
#         print("测试")
#     else:
#         return "差"



# 执行函数
# ret = my_func(60)
# print(ret)


# def my_func(score):
#     name = ""
#     # 判断
#     if score >= 90:
#         name = "优"
#     elif score >= 80:
#         name = "良"
#     elif score >= 60:
#         name = "中"
#     else:
#         name = "差"
#
#     return name
#
# print(my_func(60))


# return
# 作用 标识这一个函数有返回值
# return 返回值
# 执行完return 返回值 后面代码的不再执行 函数执行结束


# 如果在函数内部使用return 而后面没有数值
# 作用: 提前结束函数的执行
# 提供代码执行效率
def my_func(score):
    # 判断条件
    if score < 0:
        print("输入的分数不满足")
        # 提前结束函数执行的
        return
    print("测试")
    name = ""
    # 判断
    if score >= 90:
        name = "优"
    elif score >= 80:
        name = "良"
    elif score >= 60:
        name = "中"
    elif score >= 0:
        name = "差"
    return name

print(my_func(-100))


# 业务需求 执行函数的 小明 20 -> 姓名:小明 年龄:20

# # 定义一个函数
# # 返回值-> 列表
# def my_func(name, age):
#     # 构造出新的字符串
#     new_name = "姓名:" + name
#     new_age = "年龄:%d" % age
#     return [new_name, new_age]
#
# ret = my_func("小明", 20)
# print(ret[0])
# print(ret[1])


# 定义一个函数
# 返回值-> 字典
# def my_func(name, age):
#     # 构造出新的字符串
#     new_name = "姓名:" + name
#     new_age = "年龄:%d" % age
#     return {"name": new_name, "age": new_age}
#
# ret = my_func("小明", 20)
# print(ret["name"])
# print(ret["age"])


# 定义一个函数
# 返回值-> 返回值1, 返回值2,....
def my_func(name, age):
    # 构造出新的字符串
    new_name = "姓名:" + name
    new_age = "年龄:%d" % age
    return new_name, new_age

# 执行函数格式: 元组变量名 = 执行函数
ret = my_func("小明", 20)
print(type(ret))
print(ret[0])
print(ret[1])



# # 定义一个函数
# def my_func1():
#     # 定义一个局部变量
#     # 定义在函数内部的变量叫做局部变量
#     # 局部变量的作用域(使用范围)是在函数的内部
#     # 函数外部是不能使用的
#     num = 11
#     print(num)
# 执行函数
# my_func1()

# # 定义一个函数
# def my_func2():
#     # 定义一个局部变量
#     num = 11
#     print(num)


# 程序运行后执行到22行
# 内部中开辟一个空间保存20
# num = 20


# 函数中局部变量 是什么时候释放内存的
# def my_func():
#     num = 20
#
# my_func()




# 定义一个全局变量
# 定义在函数外部的变量 叫做全局变量

# num = 10
# # 定义一个函数
# def my_func1():
#     # 函数内部可以使用全局变量
#     print(num)
#
#
# def my_func2():
#     # 函数内部可以使用全局变量
#     print(num)
#
# my_func1()
# my_func2()


# # 定义了两个变量 (名字相同的变量(全局 , 局部))
# # 定义一个全局变量
# num = 10
# # 定义一个函数
# def my_func():
#     # 定义了一个和全局变量名相同的局部变量
#     # 关于函数内部使用变量的规则
#     # 当使用函数内部的变量 python会在函数内部先找这个变量(局部变量) 如果找到直接使用
#     # 如果在函数内部没找到 就会到函数外边找变量(全局变量) 直接使用
#     # 如果在函数外部也没有找到 就会报错
#     num = 20
#     print("函数内部", num)
#
#
# # 执行函数
# my_func()
# print("函数外部", num)


# 定义一个全局变量
num = 10

def my_func():
    # 在执行函数的时候 在函数内部把全局变量的值进行更改
    # 而不是创建一个和全局变量名相同的局部变量
    # 告知python 我不是创建一个新的局部变量 而是想修改全局变量
    global num
    # 全局变量的值进行修改
    num = 20
    print("内部", num)

my_func()
print("外部", num)
# 内部 20
# 外部 20


# python len
# help(len)


# 我们自己定义的函数 -> 求和
def add2num(num1, num2):
    """
    这个函数是来计算两个数字的和
    :param num1: 数字1 
    :param num2: 数字2
    :return: 返回两个数字的求和结果
    """
    return num1 + num2

# ret = add2num(10, 20)
# print(ret)
help(add2num)




