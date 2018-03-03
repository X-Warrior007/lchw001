#About the single pattern and exceptions


class Person(object):

    # 定义一个类属性保存实例对象
    __instance = None
    # 定义一个属性判断是否是第一个给对象的属性赋值
    __is_first = True

    # 重写
    def __new__(cls, *args, **kwargs):
        # 判断是不是第一次进入new方法
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)

        return cls.__instance

    # 构造方法
    def __init__(self, name, age):
        # 如果是第一次赋值
        if Person.__is_first:
            self.name = name
            self.age = age
            # 设置不是第一个
            Person.__is_first = False

    # 静态方法
    # @staticmethod
    def add2num(self,a, b):
        return a + b


xm = Person("小明", 20)

xh = Person("小红", 21)

# 保证使用当前类创建的对象的地址唯一(<__main__.Person object at 0x0000000001E9F198>)
# 只会开辟一次内存
print(xm)
print(xh)
# 保证对象的属性的值也是唯一的 对于name = 小明 age = 20
print(xm.name)
print(xh.name)

# 单例设计模式有什么用处?

p = Person("老王", 22)
print(p.add2num(10, 20))


# 异常
# FileNotFoundError: [Errno 2] No such file or directory: 'hm.txt'
# f = open("hm.txt", "r")
#
# NameError: name 'num' is not defined
# print(num)
# print(10)

# 程序上线后 用户体验 会叫产品走的更远


# FileNotFoundError:
# FileNotFoundError -> 异常类型
# [Errno 2] No such file or directory: 'hm.txt' 异常的信息描述
try:
    f = open("hm.txt", "r")
except FileNotFoundError:
    print("捕获到了异常")
    # f = open("hm.txt", "w")

"""
try:
    执行可能发生异常的代码
except 异常类型:
    如果发生异常执行的代码
"""

print("测试")


f = open("hm.txt", "w")

try:
    f = open("hm.txt", "r")
    print(num)
except (FileNotFoundError, NameError):
    print("捕获到异常")

"""
try:
    执行可能发生异常的代码(类型1)
    执行可能发生异常的代码(类型2)
    ...
except (异常类型1, 异常类型2,...):
    如果发生异常执行的代码
"""




# try:
#     f = open("hm1.txt", "r")
# except FileNotFoundError as e:
#     # 打印到异常的信息描述
#     print("捕获到了异常", e)

"""
单个异常
try:
    执行可能发生异常的代码
except 异常类型 as 临时变量(保存异常类型的信息描述):
    如果发生异常执行的代码
"""

try:
    # 如果代码发生异常后 代码将不再向下执行(try中)
    f = open("hm.txt", "r")
    print(num)
except (FileNotFoundError, NameError) as e:
    print(e)

print("测试")

"""
多个异常
try:
    执行可能发生异常的代码(类型1)
    执行可能发生异常的代码(类型2)
    ...
except (异常类型1, 异常类型2, ...) as 临时变量(保存异常类型的信息描述):
    如果发生异常执行的代码
"""




# try:
#     # f = open("hm1.txt", "r")
#     # print(num)
#     10/0
# except Exception:
#     print("捕获所有的异常类型")

"""
try:
    执行可能发生异常代码
except Exception:
    如果发生异常执行的代码
  
等价的
  
try:
    执行可能发生异常代码
except :
    如果发生异常执行的代码
"""

# try:
#     # f = open("hm1.txt", "r")
#     # print(num)
#     10/0
# except Exception as e:
#     print("捕获所有的异常类型", e)
"""
try:
    执行可能发生异常代码
except Exception as 临时变量(保存异常类型的信息描述):
    如果发生异常执行的代码
"""


try:
    print("")
except:
    print("except")
else:
    print("else")

# 如果try中的代码发生异常 会执行except 但是不会执行else

# 如果try中的代码没有发生异常 会执行else  但是不会执行except


# try:
#     print("")
# except:
#     print("except")
# else:
#     print("else")
# finally:
#     print("finally")

# 如果发生异常 try -> except -> finally
# 如果没有发生异常 try -> else -> finally

# 写法02
# try:
#     print("")
# except:
#     print("except")
# finally:
#     print("finally")

# 写法03
# try:
#     print(num)
# finally:
#     print("finally")

# try的嵌套
# 如果在内部try没有捕获异常 那么当发生异常后 会吧异常传递到外层 如果外层捕获到异常会走except方法
# 如果没有except 会发生程序崩溃
# try:
#     try:
#         f = open("hm1.txt", "r")
#     finally:
#         print("finally")
# except:
#     print("捕获到了异常")




# 函数中异常的传递
# def func1():
#     # 01 捕获异常
#     try:
#         print(num)
#     except:
#         print("except")
#
# def func2():
#     func1()
#
# def func3():
#     func2()
#
# # 执行函数
# func3()


# def func1():
#     print(num)
#
# def func2():
#     # 02 捕获异常
#     try:
#         func1()
#     except:
#         print("func2")
#
# def func3():
#     func2()
#
# # 执行函数
# func3()


# def func1():
#     print(num)
#
# def func2():
#     func1()
#
# def func3():
#     # 03 捕获异常
#     try:
#         func2()
#     except:
#         print("func3")
#
# # 执行函数
# func3()


def func1():
    print(num)

def func2():
    func1()

def func3():
    func2()

# 执行函数
try:
    func3()
except:
    print("最外面")


# NameError
# AgeError:您输入的年龄有误age=222
# 自定义异常类处理年龄输入错误
class AgeError(Exception):

    # 构造方法
    def __init__(self, age):
        self.age = age

    # str
    def __str__(self):
        return "您输入的年龄有误age=%d" % self.age

# 自定义一个人类
class Person(object):

    def __init__(self, name, age):
        # 属性赋值
        self.name = name
        # 判断
        if age <= 0 or age >= 150:
            # print("您输入的年龄有误age=%d" % age)
            # 高大尚(后期开发一些第三方模块给其他人使用)
            raise AgeError(age)
        else:
            self.age = age


# xm = Person("小明", 22)
xm = Person("小明", 222)


class Test(object):

    def __init__(self, switch):
        self.switch = switch #开关

    def calc(self, a, b):
        try:
            return a/b
        except Exception as result:
            if self.switch:
                print("捕获开启，已经捕获到了异常，信息如下:")
                print(result)
            else:
                #重新抛出这个异常，此时就不会被这个异常处理给捕获到，从而触发默认的异常处理
                raise


a = Test(False)

a.calc(11,0)












