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