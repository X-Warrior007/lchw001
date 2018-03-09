def set_func(func):
	def call_func():
		print("----这是新添加的功能：权限验证----")
		ret = func()
		print("----这是新添加的功能：log日志功能----")
		return ret
	return call_func


@set_func
def test():
	print("--------test--------")
	return 100


num = test()
print(num)