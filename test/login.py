#About print the triangle by python

"""
*
**
***
****
*****
"""
# # 定义一个变量 记录行数
# i = 1
# while i <= 5:
#     print("*")
#     i += 1

# 定义一个变量 记录列数
# j = 1
# while j <= 5:
#     print("*", end="")
#     j += 1

# 定义一个变量记录行数
i = 1
while i <= 5:
    # 定义一个变量 记录列数
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    # 换行
    print()
    i += 1
