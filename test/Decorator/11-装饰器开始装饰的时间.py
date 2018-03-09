def set_func(func):
	print("----开始用装饰器进行装饰-----")
	def call_func(*args, **kwargs):
		print("----这是新添加的功能：权限验证----")
		ret = func(*args, **kwargs)
		print("----这是新添加的功能：log日志功能----")
		return ret
	return call_func


@set_func
def test1():
	"""无参数、无返回值"""
	print("------test1-----")


# test1()
