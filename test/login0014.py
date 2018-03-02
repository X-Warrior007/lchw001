#About the forth adding of definding functions

# 打开一个文件hm.txt

# 使用读模式的方法打开文件
# 如果使用r模式打开文件 如果文件不存在将报错 如果文件存在 将打开
# 如果使用w模式打开文件 如果文件不存在 将创建一个文件打开 如果文件存在 直接打开
f = open("hm.txt", "w")
# 关闭文件(文件使用完成后)
f.close()



# <1>写数据(write)
# 打开文件 写入数据
# f = open("hm.txt", "w")
# f.write("hello")
# f.close()

# <2>读数据(read) -> 读取文件中的所有数据
# 打开文件
# f = open("hm.txt", "r")
# ret = f.read()
# print(ret)
# f.close()
# 读取he
# read(num) 代表读取num个字节
# ret = f.read(2)
# print(ret)
# f.close()

# <3>读数据（readlines）
# 把文件中的数据分行读取后保存到列表中
# f = open("hm.txt", "r")
# ret = f.readlines()
# print(ret)
# f.close()

# <4>读数据（readline）
# f = open("hm.txt", "r")
# ret = f.readline()
# print(ret)
# ret = f.readline()
# print(ret)
# ret = f.readline()
# print(ret)
# f.close()


# w 写入数据
# 当如果使用写模式打开文件 先把文件中的内容清空 然后在写入
# f = open("hm.txt", "w")
# f.write("q")
# f.close


# a -> append -> 追加数据
# f = open("hm.txt", "a")
# f.write("hello")
# f.close()



# 了解
"""
# 美国人 -> 计算机 a -> 97
# ASCII码 编码对应表 a -> 97
# 计算机只认识(0和1-> 二进制) 
# 一共300多个数据就可以全部表达了键盘中的字母 或者各种字符
# ASCII码 只能满足美国人的开发
# 中国 -> 汉字
# GBK(97 -> 中) -> 简体
# GBK 收录到汉字 30k 汉字90k
# BIG5 繁体

# 国际非盈利组织 unicode(万国码)-> 包含了所有的国家的文字
# unicode每天都更新
# 保存这些数据占用的存储空间很大
# unicode升级版utf-8
# 每个字母 占一个字节 每个中文占3个字节

"""
# 如果写入的数据有中文(Windows中)
# f = open("hm.txt", "w", encoding="utf-8")出现在Windows中
# 不是所有的window电脑都是gbk编码
# 如果是linux 或者mac 不需要考虑
# f = open("hm.txt", "w", encoding="utf-8")
# f.write("中国")
# f.close()

# 读取数据
# f = open("hm.txt", "r", encoding="utf-8")
# ret = f.read()
# print(ret)
# f.close()

# 以上的无论是a r w 都是文本数据(字符串)
# 保存数据的方式不同 一个是文本 一个是二进制

# 写入数据二进制
# f = open("hmhm.txt", "wb")
# # 指定编码格式 保存的二进制字符串
# 编码
# f.write("中国".encode("utf-8"))
# f.close()

# 读取数据二进制
# f = open("hmhm.txt", "rb")
# 解码
# 中文使用二进制保存 是三个
# 如果是文本方式 一个中文还是一个字节
# ret = f.read(3).decode(encoding="utf-8")
# print(ret)
# f.close()


# 写输入到文件中
# f = open("hm.txt", "w")
# f.write("tyuiolkjhjklskjsklghuijjhbjkjnkl")
# f.close()

# 边读边写
f = open("hm.txt", "r")
# ret = f.read(5)
# print(ret)
# ret = f.read(5)
# print(ret)
# ret = f.read(5)
# print(ret)
# ret = f.read(5)
# if len(ret)> 0:
#     print(ret)

new_f = open("hm[备份].txt", "w")

# 死循环
while True:
    # 读取数据
    ret = f.read(5)
    if len(ret)> 0:
        new_f.write(ret)
    else:
        break
# 关闭文件
f.close()
new_f.close()

# 导入模块
import os

# 1. 文件重命名
#
# os模块中的rename()可以完成对文件的重命名操作
#
# rename(需要修改的文件名, 新的文件名)
# os.rename("hm.txt", "hmhm.txt")


# 2. 删除文件
#
# os模块中的remove()可以完成对文件的删除操作
#
# remove(待删除的文件名)
# os.remove("hm[备份].txt")

# 3. 创建文件夹
# os.mkdir("黑马文件夹")

# 4. 获取当前目录
# 02-文件的相关操作.py 他属于哪个文件夹? 第九天的代码
# Z:\Desktop\第九天的代码
print(os.getcwd())

# Z:\Desktop\第九天的代码
# 5. 改变默认目录
# os.chdir("黑马文件夹")
# print(os.getcwd())

# 无论是../ 或者是./ 都叫做相对路径
# ../ 返回到上一级目录
# ./ 就代表的是当前目录
# 绝对路径: Z:\Desktop\第九天的代码 绝对路径是有盘符
# os.chdir("./")
# print(os.getcwd())


# 6. 获取目录列表
# ret = os.listdir()
# print(ret)


# 7. 删除文件夹
# os.rmdir("黑马文件夹")

# 创建一个文件夹-> 黑马文件夹
# 在黑马文件夹里面创建10个文件hm1.txt hm2.txt..hm10.txt
# 对黑马文件夹hm1.txt 就行文件名修改  hm1[龟叔].txt..hm10[龟叔].txt
import os
# 定义一个变量记录
file_name = "黑马文件夹"
# 01 创建一个文件夹
# FileExistsError: [WinError 183] 当文件已存在时，无法创建该文件。: '黑马文件夹'
# os.path.exists(file_name) 判断一个文件或者文件夹是否存在
# if not os.path.exists(file_name):
#     os.mkdir(file_name)
#
# # 修改默认目录
# os.chdir(file_name)
# # 02 创建10个文件
# for i in range(1, 11):
#     f = open("hm%d.txt" % i, "w")
#     f.close()


# 批量修改文件夹中文件名
# # 修改默认目录
os.chdir(file_name)
print(os.getcwd())
# 获取file_name文件夹下的所有的文件的名字
my_list = os.listdir()
# 遍历依次修改文件名
for value in my_list:
    # hm1.txt -> hm1[龟叔].txt
    new_name = value.replace(".txt", "[龟叔].txt")
    # 进行修改
    os.rename(value, new_name)






