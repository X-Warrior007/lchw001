
# 带有yield关键字的函数就是生成器函数
def hello():
    yield 1
    yield 2


# 调用生成器函数产生生成器对象
h = hello()
# F7步进 F8步过
print(next(h))
print(next(h))