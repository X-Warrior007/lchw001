def set_func(func):
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


@set_func
def test2():
	"""无参数、有返回值"""
	print("------test2-----")
	return 200


@set_func
def test3(num1, num2):
	"""有参数、无返回值"""
	print("------test3--num1=%d,num2=%d---" % (num1, num2))


@set_func
def test4(num):
	"""有参数、有返回值"""
	print("------test4--num=%d---" % num)
	return "400000000"


test1()
print("*"*30)

num2 = test2()
print(num2)
print("*"*30)

test3(100, 200)
print("*"*30)

num4 = test4(400)
print(num4)
print("*"*30)