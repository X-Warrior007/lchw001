import time


def set_log(log_level):  # 用来设置参数
	def set_func(func):  # 用来保存原函数的引用
		def call_func(*args, **kwargs):  # 用来添加新功能，并且调用原函数

			log_level_info_dict = {
				1: "warning",
				2: "error"
			}

			with open("./log.txt", "a") as f:
				f.write("--(%s)--%s---调用了(%s)函数\n" % (log_level_info_dict[log_level], time.ctime(), func.__name__))
			return func(*args, **kwargs)
		return call_func
	return set_func


# 如果@set_log后面跟上一个括号()然后在括号中有参数 的话，那么这样的装饰器就表示带有参数的装饰器
# 带有参数的装饰器，装饰的流程如下：
# 1. 先调用set_log函数，并且把1当做实参进行传递
# 2. 把set_log函数的返回值，当做装饰器来对test函数进行装饰（其装饰的过程 与之前普通装饰器装饰的过程一样）
@set_log(1)  
def test():  # 相当于 test = set_func(test)
	print("-----test----")


@set_log(2)
def test2():
	print("-----test2----")


test()
test2()