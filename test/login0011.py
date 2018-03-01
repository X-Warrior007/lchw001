# 函数是对多行(也可能是一行)代码进行封装
# 函数就是对某个功能的解释

def my_print():
    print("                            _ooOoo_  ")
    print("                           o8888888o  ")
    print("                           88  .  88  ")
    print("                           (| -_- |)  ")
    print("                            O\\ = /O  ")
    print("                        ____/`---'\\____  ")
    print("                      .   ' \\| |// `.  ")
    print("                       / \\||| : |||// \\  ")
    print("                     / _||||| -:- |||||- \\  ")
    print("                       | | \\\\\\ - /// | |  ")
    print("                     | \\_| ''\\---/'' | |  ")
    print("                      \\ .-\\__ `-` ___/-. /  ")
    print("                   ___`. .' /--.--\\ `. . __  ")
    print("                ."" '< `.___\\_<|>_/___.' >'"".  ")
    print("               | | : `- \\`.;`\\ _ /`;.`/ - ` : | |  ")
    print("                 \\ \\ `-. \\_ __\\ /__ _/ .-` / /  ")
    print("         ======`-.____`-.___\\_____/___.-`____.-'======  ")
    print("                            `=---='  ")
    print("  ")
    print("         .............................................  ")
    print("                  佛祖镇楼                  BUG辟易  ")
    print("          佛曰:  ")
    print("                  写字楼里写字间，写字间里程序员；  ")
    print("                  程序人员写程序，又拿程序换酒钱。  ")
    print("                  酒醒只在网上坐，酒醉还来网下眠；  ")
    print("                  酒醉酒醒日复日，网上网下年复年。  ")
    print("                  但愿老死电脑间，不愿鞠躬老板前；  ")
    print("                  奔驰宝马贵者趣，公交自行程序员。  ")
    print("                  别人笑我忒疯癫，我笑自己命太贱；  ")
    print("                  不见满街漂亮妹，哪个归得程序员？")

# my_print()
# num = 3.4567890
# #
# print("哈哈哈")
# my_print()
# a = 10
# for i in range(10):
#     my_print()
# b = 10
# 打印佛祖镇楼

# 函数的定义:
# def -> define
# 格式: def 函数名():
def my_print():
    print("hello")
    print("world")
    print("你好")
    print("python")

# 函数的执行(函数调用)
# 格式: 函数名()
# my_print()
# 如果函数名相同 那么最后一个存在
my_print()


# # 计算两个数的和  10  6  = 16 打印
# def my_func():
#     a = 10
#     b = 6
#     print(a + b)
#
# my_func()
#
# # 计算两个数的和 20 + 16 = 36 打印
# def my_func1():
#     a = 20
#     b = 16
#     print(a + b)
#
# my_func1()
# 有参数函数的定义:
# 形参 -> 形式参数
# 格式: def 函数名(参数1(形参), 参数2, ...)
# 形参只能在函数内部使用
# 形参使用的作用域 (范围)
def my_func(a, b):
    print(a + b)

# 函数的执行
# 执行有参数的函数的格式:
# 实参 =  实际参数
# 格式: 函数名(参数1(实参), 参数2,...)
# my_func(10, 6)
# my_func(20, 16)

# python中 是引用传递 不是值得传递
# 变量
num1 = 10
num2 = 6
my_func(num1, num2)



# 定义一个有参数和又返回值的函数
# 格式: def 函数名(参数1, 参数2,...):
#             代码逻辑
#             return 返回值
def my_func(a, b):
    my_sum = a + b
    return my_sum

# 执行函数
# 格式: 变量名 = 函数名(参数1, 参数2,....)
ret1 = my_func(10, 6)
# 就想在第八行打印
print(ret1)

# 4种函数的类型
# 无参数无返回值
# 无参数有返回值
# 有参数无返回值
# 有参数有返回值

# 想打印一句话 你好龟叔 使用函数完成
# 无参数无返回值的函数
# 格式: def 函数名():
# def my_func():
#     print("你好龟叔")


# 执行函数
# 格式: 函数名()
# my_func()

# 输出你好XX 在我执行函数的时候确定XX是什么
# 有参数无返回值的函数
# 格式: def 函数名(参数1, 参数2, ...):
# def my_func(xx):
#     print("你好%s" % xx)

# 执行函数
# 格式: 函数名(参数1, 参数2, ...)
# my_func("世界")

# 打印一句话 3.1415926
# 无参数有返回值的函数
# 格式: def 函数名():
#             代码逻辑
#             return 返回值
# def my_func():
#     a = 3.1415926
#     return a
#
# # 执行函数
# # 格式: 变量名 = 函数名()
# ret = my_func()
# print(ret)

# 模拟计算一个字符串的长度 借助函数
# 有参数又返回值的函数
# 格式: def 函数名(参数1, 参数2,...):
#             代码逻辑
#             return 返回值
def my_len(o):
    a = o
    i = 0
    for c in a:
        i += 1
    return i

# 执行函数
# 格式: 变量名 = 函数名(参数1, 参数2, ...)
ret = my_len("hello")
print(ret)




# python结构
# 变量 -> 函数 -> 类 -> 模块 -> 包(不一定) -> 项目


# 定义两个简单的函数
# def my_func1():
#     print("A")
#     my_func2()
#     print("B")
#
# def my_func2():
#     print("C")
#     print("D")
#
# my_func1()

# 执行my_func1 ->进入my_func1 -> 执行my_func2 -> 进入my_func2 -> 离开my_func2 -> 离开my_func1 -> 在执行测试
# print("测试")

# A C D B 测试

# 函数的嵌套
def my_func1():
    print("A")
    def my_func2():
        print("哈哈")
    my_func2()
    print("B")

my_func1()



# 自定一个打印一条横线
# def my_print(num):
#     print("-"*num)

# my_print(20)
# 打印10行 每行有20根-
# for i in range(10):
#     # 函数的调用
#     my_print(20)



# 写一个函数求三个数的和
def my_sum(a, b, c):
    return a + b + c

# aa = 10
# bb = 20
# cc = 30
# 把变量作为实参传入函数中给形参(引用)
# ret = my_sum(aa, bb, cc)
# print(ret)

# 写一个函数求三个数的平均值
# def average3Number(num1, num2, num3):
#     # 把average3Number函数的形参作为my_sum实参传入函数中作为my_sum的形参
#     sum = my_sum(num1, num2, num3)
#     return sum/3
#
# aa = 10
# bb = 20
# cc = 30
# result = average3Number(aa, bb, cc)
# print(result)


# 定义一个函数
# def print_info(name, age, no):
#     print(name)
#     print(age)
#     print(no)

# 执行函数
# 执行函数使用的是位置参数(实参和形参的位置是一一对应的)
#
# print_info(22, "小明", "009")

# python是属于弱类型
# 通过自己的能力来判断参数类型的选择
# 询问函数的定义这 参数类型如何选择
# def my_func(a, b):
#     return a + b
#
# # print(my_func("10", 20))

def print_info(name, age, no):
    print(name)
    print(age)
    print(no)

# 位置参数
# print_info("小明", 20, "009")

# 关键字参数(形参的名字)
# 不需要考虑位置 只要关键字正确即可
# print_info(no="009", age=20, name="小明")

# 假如执行函数使用位置参数和关键字参数
print_info("小明", no="009", age=20)



