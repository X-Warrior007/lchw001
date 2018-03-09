class Log(object):
	def __init__(self, func):
		self.func = func

	def __call__(self, *args, **kwargs):
		print("-----call被调用----")
		return self.func(*args, **kwargs)


@Log  # 等价于test = Log(test)  # 想一想：如果是@Log(1)那么应该怎样理解？ 提示：按照普通的带有参数的装饰器去理解一下
def test():
	print("-----test----")


test()
