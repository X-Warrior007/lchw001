def set_func(func):
	def call_func():
		print("----这是新添加的功能：权限验证----")
		func()
		print("----这是新添加的功能：log日志功能----")
	return call_func


@set_func
def test():
	print("--------test------没有参数 没有返回值----")


test()