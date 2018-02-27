#About using of strings

# 定义一个字符串
# str1 = "helloworld"
# str2 = 'helloworld'
# if str1 ==  str2:
#     print("哈哈")

# 定义特殊的字符串 空字符串
# str3 = ""
# str4 = str()
# python中内置函数 4len()
# o == object -> 对象 -> python中万物皆对象
# l = len(str4)
# print(l)

# 如果在开始中 需要保留文本的格式的时候 我们可以使用三引号的字符串
# str5 = """hello
# world
# 哈哈

# 定义一个字符串(有序的字符序列)
a = "abcdef"

# 通过下标索引获取字符串中的指定的字符(从左到右来得到的下标 0, 1, 2, n)
# ret1 = a[4]
# print(ret1)

# 如果是从右侧到左侧 是从 -1, -2, -3, -n
# ret2 = a[-2]
# print(ret2)

# 切片的语法：[起始:结束:步长]
# >>> a = "abcdef"

# 已有的字符串
a = "abcdef"
#  'abc' -> a[0:3] == a[:3]
# ret1 = a[:3]
# # 因为python字符串是不可变的
# print(a)
# print(ret1)

#  'ace' -> a[:5:2]  或者 a[::2]
# ret2 = a[:5:2]
# print(ret2)

#  'bd'
# ret3 = a[1:5:2]
# print(ret3)


#  'fdb' 如果步长为负数 代表的是倒序
# ret4 = a[::-2]
# print(ret4)


#  'fd'
# ret5 = a[-1:-4:-2]
# print(ret5)

a = "bcaeaf"

# <1>find
# 检测 str 是否包含在 mystr中，如果是返回开始的索引值，否则返回-1
# ret1 = a.find("3bc")
# print(ret1)

# <2>index
# 跟find()方法一样，只不过如果str不在 mystr中会报一个异常.
# ret2 = a.index("bg")
# print(ret2)

# <3>count
# 返回 str在start和end之间 在 mystr里面出现的次数
# count = a.count("a")
# print(count)

# <4>replace
# 把 mystr 中的 str1 替换成 str2,如果 count 指定，则替换不超过 count 次.
# ret4 = a.replace("a", "A")
# print(ret4)

# <5>split
# 以 str 为分隔符切片 mystr，如果 maxsplit有指定值，则仅分隔 maxsplit 个子字符串
# ret5 = a.split("a")
# print(ret5)

# <6>capitalize
# 把字符串的第一个字符大写
# ret1 = a.capitalize()
# print(ret1)

# <7>title
# 把字符串的每个单词首字母大写
# ret2 = a.title()
# print(ret2)

# <8>startswith
# 检查字符串是否是以 hello 开头, 是则返回 True，否则返回 False
# ret3 = a.startswith("aaa")
# print(ret3)

# <9>endswith
# 检查字符串是否以obj结束，如果是返回True,否则返回 False
# ret4 = a.endswith(".MP3")
# print(ret4)

# <10>lower
# 转换 mystr 中所有大写字符为小写
# ret5 = a.lower()
# print(ret5)

# <12>ljust
# 返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
# ret1 = a.ljust(10, " ")
# print(ret1)

# <13>rjust
# 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
# ret2 = a.rjust(10, "x")
# print(ret2)

# <14>center
# 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
# ret3 = a.center(10, "h")
# print(ret3)

# <15>lstrip
# 删除 mystr 左边的空白字符
# ret4 = a.lstrip("xacb")
# print(ret4)

# <16>rstrip
# 删除 mystr 字符串末尾的空白字符
# ret5 = a.rstrip("s")
# print(ret5)

# <17>strip
# 删除mystr字符串两端的空白字符
# ret6 = a.strip("xs")
# print(ret6)

# <18>rfind
# 类似于 find()函数，不过是从右边开始查找.
# ret1 = a.rfind("f")
# print(ret1)

# <19>rindex
# 类似于 index()，不过是从右边开始.

# <20>partition
# 把mystr以str分割成三部分,str前，str和str后
# ret3 = a.partition("a")
# ('', 'a', 'bcdfef') 元组
# print(ret3)

# <21>rpartition
# 类似于 partition()函数,不过是从右边开始.
# ret4 = a.rpartition("d")
# print(ret4)

# <22>splitlines
# 按照行分隔，返回一个包含各行作为元素的列表
# ret5 = a.splitlines()
# print(ret5)

# <23>isalpha
# 如果 mystr 所有字符都是字母 则返回 True,否则返回 False
# ret1 = a.isalpha()
# print(ret1)

# <24>isdigit
# 如果 mystr 只包含数字则返回 True 否则返回 False.
# ret2 = a.isdigit()
# print(ret2)

# <25>isalnum
# 如果 mystr 所有字符都是字母或数字则返回 True,否则返回 False
# ret3 = a.isalnum()
# print(ret3)

# <26>isspace
# 如果 mystr 中只包含空格，则返回 True，否则返回 False.
# ret4 = a.isspace()
# print(ret4)

# <27>join
# mystr 中每个元素后面插入str,构造出一个新的字符串
# 定义一个列表
# my_list = ["1", "2", "3"]
# # 最终打印结果"1x2x3"
# ret5 = "".join(my_list)
# print(ret5)

# acdef
# ['a', 'c', 'd', 'e', 'f']
a = "abcbdbebf"
ret6 = a.split("b")
ret7 = "".join(ret6)
print(ret7)

# # python中 提供了一个函数 help
# a = "abc"
# str
# # print(type(a))
# # a.
# # help(str.count)
