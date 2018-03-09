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


# 想一想：如果是@Log(1)那么应该怎样理解？ 提示：按照普通的带有参数的装饰器去理解一下
# 1. 先调用Log(1)然后用这个Log(1)的返回值 当做装饰器来装饰
# Log(1)意味着什么？--->创建一个实例对象----->返回的是这个实例对象的引用
class Log(object):
	def __init__(self, num):
		self.num = num

	def __call__(self, func):
		self.func = func
		return self.call_func

	def call_func(self, *args, **kwargs):
		print("这里是需要添加的新功能")
		return self.func(*args, **kwargs)


# 2. 拿着实例对象的引用去给test函数进行装饰, 可以理解为test = 实例对象(test)
# 实例对象(test)----->调用实例对象，那么也就意味着调用__call__方法
# 让test指向 __call__方法的返回值
# 最终，让test指向了 call_func方法
# 
# 当再次调用test()的时候，实际上是调用的call_func方法










