def set_pri(func):
	print("----开始用装饰器进行装饰(权限验证)-----")
	def call_func(*args, **kwargs):
		print("----这是新添加的功能：权限验证----")
		ret = func(*args, **kwargs)
		return ret
	return call_func


def set_log(func):
	print("----开始用装饰器进行装饰(log日志功能)-----")
	def call_func(*args, **kwargs):
		print("----这是新添加的功能：log日志功能----")
		ret = func(*args, **kwargs)
		return ret
	return call_func


@set_pri  # 这是权限的验证
@set_log  # 这是log日志
def test1():
	"""无参数、无返回值"""
	print("------test1-----")


test1()
