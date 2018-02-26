#About print the multiplication table which is 9*9 by python
# while嵌套应用二：九九乘法表

# 定义一个变量 记录行数
# i = 1
# while i <= 9:
#     print(i)
#     i += 1

# 定义一个变量 记录列数
# j = 1
# while j <= 3:
#     print(j, end="")
#     j += 1

# 定义一个变量 记录行数
i = 1
while i <= 9:
    # 定义一个变量 记录列数
    j = 1
    while j <= i:
        print("%d * %d = %-2d" % (j, i, i * j), end="  ")
        j += 1
    # 换行
    print()
    i += 1
