def set_func(func):
	def call_func():
		print("----这是新添加的功能：权限验证----")
		func()
		print("----这是新添加的功能：log日志功能----")
	return call_func


@set_func  # 等价于test = set_func(test)
def test():
	print("------test------")


# test = set_func(test)
# test()

# class T(object):
# 	@staticmethod  # 等价于 test = staticmethod(test)
# 	def test():
# 		pass

test()


# 注意点
# 1. 装饰器只能在原函数之前或者之后添加新功能，不能在原函数中间添加新功能
# 2. 装饰只需要1次，但是剩下所有的调用 都是调用的装饰之后的样子