
# for i in data:
#   print(i)

data = [1,2,3,4,5]
# 1 取出data_list的首元素位置到记录者中
# iter(可迭代对象)获取一个可迭代对象的 提供的迭代器
data_iter = iter(data)
while True:
    # 2 判断当前元素是否已经取完成
    # 3 完成则结束 ; 否则取记录者标识的元素
    # 4 记录者记录下一个元素的位置
    try:
        # 通过迭代自动访问指向的元素 并且通过函数返回值 返回遍历到的元素的值
        # 自动指向下一个元素的相关位置
        i = next(data_iter)
    except Exception as e:
        break
    else:
        print(i)