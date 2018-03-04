#About models and relatives  

# 导入模块
# 格式: import 模块名
import hm_sum

# 使用格式: 模块名.全局变量 模块名.函数名 模块名.类名
print(hm_sum.name)

print(hm_sum.my_sum(10, 20))

print(hm_sum.Person())

# 选择性的导入模块的全局变量 还是函数 还是类
# 格式: from 模块名 import 全局变量 或者函数 或者类
# from hm_sum import name


# 缺点: 如果模块中的全局变量 还是函数 还是类 的名字冲突
# 优点: 可以不写模块名
# name = 10
# print(name)

# 把该模块中的全局变量 或者函数 或者类全部导入 和import相似
# from hm_sum import * 和import 模块名 差异 一个需要先写模块名(import 模块名) 一个不需写(from hm_sum import *)
from hm_sum import *
print(name)
print(my_sum(10, 20))
print(Person())


# 导入一个模块
# 格式: import 模块名 as 模块名的别名
# import hm_sum as hmhm_sum
#
# print(hmhm_sum.name)
# print(hmhm_sum.Person)

# 使用as 可以给模块 或者是全局变量 或者是函数 或者是类名 起一个别名 防止跟本模块中名字冲突
from hm_sum import n
ame as my_name
print(my_name)



# 如果__all__ 和 from 模块名 import * 配合使用 限制模块中那些全局变量 或者 函数 或者是类可以使用
# 导入
from hmhm_sum import *
# print(name)


# 导入包中的模块
# import hmhm.hmhmhm
# # 使用的时候
# print(hmhm.hmhmhm.my_name)


# from hmhm.hmhmhm import *
#
# print(my_name)

# import hmhm.hmhmhm as hm_hm

# print(hm_hm.my_name)

# 全局变量
name = "加法运算"

# 加法运算
# 定义一个函数
def my_sum(a, b):
    return a + b

# 定义一个类
class Person(object):
    pass


# 先需要自测
# 一般需要创建一个函数 来完成自测
def main():
    # 定义一个变量
    ret = my_sum(10, 20)
    print(ret)

# 执行函数

# 默认情况下 在本模块内执行这个模块 当前的这个python的变量__name__ 的值为 __main__

# print(__name__)

# 书写格式 一般都会这么写 (开发常用于"测试" 或者作为程序的入口)
if __name__ == '__main__':
    main()



# python中的变量
__all__ = ["name", "Person"]

# 全局变量
name = "加法运算"

# 加法运算
# 定义一个函数
def my_sum(a, b):
    return a + b

# 定义一个类
class Person(object):
    pass


# 先需要自测
# 一般需要创建一个函数 来完成自测
def main():
    # 定义一个变量
    ret = my_sum(10, 20)
    print(ret)

# 执行函数

# 默认情况下 在本模块内执行这个模块 当前的这个python的变量__name__ 的值为 __main__

# print(__name__)

# 书写格式 一般都会这么写 (开发常用于"测试" 或者作为程序的入口)
if __name__ == '__main__':
    main()
