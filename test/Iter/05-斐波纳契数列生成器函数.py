def Fib(n):
    index = 0
    number1,number2 = 0,1

    while index<n:
        number = number1
        number1,number2 = number2, number1 + number2
        index += 1
        num = yield number
        print("接收到信息%s" % num)
        # yield关键字的两个作用  1 挂起 返回值
        # 2 恢复函数(可以接收额外的参数赋值给等号左边可能存在的变量)继续紧接执行
    return 9999

# 调用生成器函数产生生成器对象
f = Fib(10)

# 生成器内部已经自带了迭代器相关的功能(支持__iter__ __next__ 抛出异常) 所以是一种特殊的迭代器
# for i in f:
#     # i = next(f) 《---- number
#     print(i)
while True:
    try:
        i = next(f)
    except StopIteration as e:
        print(e.value)
        break
    else:
        print(i)
