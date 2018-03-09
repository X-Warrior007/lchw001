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
	return [100, 200]  # return其实有2个功能：1. 返回一个数据 2.结束函数的运行
	return [3, 4]


num = test()
print(num)