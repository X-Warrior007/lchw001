#About using of some keywords

# if 和else
# 定义两个变量
# 定义到的长度
daoLenght = 8
chePiao = 0
# 判断危险品
if daoLenght < 10:
    print("可以进入火车站")
    # 检查车票
    if chePiao == 1:
        print("可以上车")
    else:
        print("请买票在上车")
else:
    print("请带着你的宝剑离开")

#  while和break
# 结论: 如果while循环和break 配合使用 当执行完break 会提前结束循环(终止循环)
# break后面的代码也不会执行
# i = 0
# while i < 5:
#     print(i)
#     if i == 2:
#         break
#         print("哈哈")
#     i += 1
#
# print("测试")


# while循环和continue 配合使用
# 结论: 如果while和continue配合使用 会提前结束本次循环 而且continue 后面的代码不会执行
# i = 0
# while i < 5:
#     i += 1
#     if i == 2:
#         continue
#         print("哈哈")
#     print(i)
#
# print("测试")


# for循环和break
# for循环和break 结果和while一样的
# for i in range(5):
#     if i == 2:
#         break
#     print(i)

# for循环和continue
# for循环和continue 结果和while一样的
# for i in range(5):
#     if i == 2:
#         continue
#     print(i)

# # for-else
# # for循环
# # 如果当前for-else配合使用 for循环正常结束 然后会走else中的代码 然后执行for-else后面的代码
# for i in range(5):
#     print(i)
# else:
#     print("else")
# print("测试")


# # for-else-break
# # 如果for循环中 执行了break 那么else中代码将不会执行
#
# for i in range(5):
#     print(i)
#     if i == 2:
#         break
# else:
#     print("else")
# print("测试")


# for-else-continue
# 如果for循环中continue 结果和for循环中没有任何关键字(break) 的结果是一样的

# for i in range(5):
#     if i == 2:
#         continue
#     print(i)
# else:
#     print("else")
# print("测试")


# #while-else
# # 和for-else一样的
# i = 0
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print("else")
# print("测试")

#while-else-break
# 和for-else-break结果是一样的
# i = 0
# while i < 5:
#     print(i)
#     if i == 2:
#         break
#     i += 1
# else:
#     print("else")
# print("测试")


#while-else-continue
# 和for-else-continue的结果是一样的
i = 0
while i < 5:
    print(i)
    i += 1
    if i == 2:
        continue

else:
    print("else")
print("测试")
