# coding=utf-8


def line_6(k, b):
	# count_num = 0  # 用来统计运行次数
	count_num = [0]
	def create_y(x):
		# nonlocal count_num
		# count_num += 1
		count_num[0] += 1
		print("这是第%d次执行，当x=%d时，y=%d" % (count_num[0], x, k*x+b))
	return create_y

line_6_1 = line_6(1, 2)  # 创建一个新的闭包，让line_6_1指向
# print(id(line_6_1))
line_6_1(0)
line_6_1(1)
line_6_1(2)
# line_6_2 = line_6(11, 22)  # 创建另外一个新的闭包，让line_6_2指向
# print(id(line_6_2))
# line_6_2(0)
# line_6_2(1)
# line_6_2(2)