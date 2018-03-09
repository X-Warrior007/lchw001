def set_func(func):
	def call_func(*args, **kwargs):  # 在定义的时候，*和**告诉python解释器 args、kwargs有特殊功能，args以元组的方式存储多余的数值， kwargs以字典的方式存储多余的命名参数
		print("----这是新添加的功能：权限验证----")
		func(*args, **kwargs)  # *和**除了在定义的时候，都意味着 进行拆包， 想一想：func(args, kwargs)?????
								# *args意味着，例如将 (100, 200)变为100, 200
								# **kwargs 意味着，例如将{"num1": 100, "num2":200}变为num=100, num2=200
								# func(*args, **kwarg)--->func(100, 200, num1=100, num2=200)
								#
								# 如果调用的时候是func(args, kwargs)？
								# func(args, kwargs)----->func((100, 200), {"num1": 100, "num2":200})
		print("----这是新添加的功能：log日志功能----")
	return call_func


@set_func
def test(num):
	print("----num=%d----" % num)


@set_func
def test2(num1, num2):
	print("----num1=%d-num2=%d---" % (num1, num2))


test(100)
test2(100, 200)