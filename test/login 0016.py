#About the using of class



# 定义一个空列表my_list 对象
# python中提供一个类list类通过list类创建一个对象
# my_list = list()
# 创建一个小明这个对象 -> Person (自定义类)

# class Person: class Person(): 经典类
# class Person(object): 新式类
#python2.x中class Person: class Person(): 没有父类的
# class Person(object): 新式类 -> 重写(魔法方法)
# 自定义一个人类
# class Person:
#     pass
#
# class Person():
#     pass

# class 自定义一个类
# 类名 命名规则: 遵循大驼峰
# 格式: class 类名(object):
class Person(object):
    pass
# 以上三种方式自定义类 在python3.x中都是一样的 都是继承与object类
# object 类 -> 所有类的父类(基类)


# 自定义类 -> 黄忠(对象) -> 通过一个英雄类
class Hero(object):

    # 实例方法*
    # 对象方法
    # 会走
    # 方法的第一个形参是self
    def move(self):
        print("英雄会走")


# 定义一个列表
# my_list = list()
# my_list.sort()
# 通过英雄类创建出一个英雄-> 黄忠
huangzhong = Hero()
# python的执行的格式 对象名.方法名
# "."点语法来执行实例方法
huangzhong.move()


# def my_func():
#     print("测试")
#
# my_func()
#


# 自定义一个英雄类
class Hero(object):

    # 会走
    def move(self):
        print("英雄会走")

# 定义一个 对象
huangzhong = Hero()
# 属性 名字 年龄 血量 攻击力
# 给对象添加属性
huangzhong.name = "黄忠"
huangzhong.age = 800
huangzhong.hp = 4000
huangzhong.atk = 400
huangzhong.move()

# 获取对象的属性
print(huangzhong.name)
print(huangzhong.age)
print(huangzhong.hp)
print(huangzhong.atk)


# 自定义一个英雄类
class Hero(object):

    # 会走
    def move(self):
        print(id(self))
        print("英雄会走")

    # 定义一个实例方法
    def info(self):
        #如果在类内部的函数中打印对象的属性
        # 格式:self.属性名
        print(self.name)
        print(self.age)
        print(self.hp)
        print(self.atk)


# 定义一个 对象
huangzhong = Hero()
# 属性 名字 年龄 血量 攻击力
# 给对象添加属性
huangzhong.name = "黄忠"
huangzhong.age = 800
huangzhong.hp = 4000
huangzhong.atk = 400
# 在使用对象执行类中的实例方法 实例方法中的第一个形参是对象
# 默认情况下 在使用对象执行实例方法的时候对象对作为实参传入到实例方法中 但是不需要传递
huangzhong.move()
# 如果直接打印一个自定义对象 那么输出的为是一个16进制的地址
# 通过id查看对象的地址
print(id(huangzhong))
# 打印对象的信息
huangzhong.info()
# 获取对象的属性

def print_info():
    # 如果在类的外面 想打印一个对象的属性
    # 格式: 对象名.属性名
    print(huangzhong.name)
    print(huangzhong.age)
    print(huangzhong.hp)
    print(huangzhong.atk)

print_info()



# 自定义一个类 (创建出一个旺财这个狗)
class Dog(object):
    # 魔法方法: 是python提供的
    # 特点: 以两个下划线开始 然后以两个下滑线的的方法 称之为魔法方法
    # 魔法方法的作用: 当程序员自定义了一个类 然后实现了(重写)魔法方法
    # 在特殊的情况下 会被python执行
    # 实现了魔法方法 监听到对象什么时候创建完成

    def __init__(self):
        # 标识这对象已经创建成功
        print("哈哈")
        # 名字 毛色
        self.name = "旺财"
        self.color = "黄色"

    # 吃骨头
    def eat(self):
        print("吃骨头")

    # 打印属性值
    def info(self):
        print("名字:%s" % self.name)
        print("毛色:%s" % self.color)


# 创建旺财
# 张三家的狗
wangcai1 = Dog()

# 打印信息
wangcai1.info()

print("="*30)

# 李四家的狗 -> 旺财  黄色
wangcai2 = Dog()

# 打印信息
wangcai2.info()

print("="*30)
# 李四家的狗 -> 旺财  黄色

wangcai3 = Dog()

# 打印信息
wangcai3.info()



# 自定义一个类 (创建出一个旺财这个狗)
class Dog(object):

    # 构造方法(构造函数)
    def __init__(self, new_name, new_color, new_age=10):
        # 标识这对象已经创建成功
        print("哈哈")
        # 名字 毛色
        self.name = new_name
        self.color = new_color
        self.age = new_age

    # 吃骨头
    def eat(self):
        print("吃骨头")

    # 打印属性值
    def info(self):
        print("名字:%s" % self.name)
        print("毛色:%s" % self.color)
        print("年龄:%d" % self.age)




# 创建一个属性name藏獒 color黑色
zangao = Dog("藏獒", "黑色")
zangao.info()

# 创建一个 斗牛犬 白色
douniu = Dog("斗牛犬", "白色")
douniu.info()


# 创建一个旺财 黄色 20
wangcai = Dog("旺财", "黄色", 20)
wangcai.info()

# 如果

# def my_func(x):
#     print(x)
# my_func()



# 自定义类 人  名字 年龄 学号
class Person(object):

    # 构造方法
    def __init__(self, name, age, no):
        # 添加属性
        self.name = name
        self.age = age
        self.no = no

    # 打印信息
    def info(self):
        print("姓名:%s" % self.name)
        print("年龄:%d" % self.age)
        print("学号:%s" % self.no)

    # 实现一个魔法方法
    # 魔法方法中 不可以在加形参
    # 返回一个字符串
    # 作用: 方便开发
    def __str__(self):
        return "姓名:%s 年龄:%d 学号:%s" % (self.name, self.age, self.no)


# 自定义对象 小明 22 008
xiaoming = Person("小明", 22, "008")
# xiaoming.info()
# 默认情况下 打印自定义对象的时候 回输出 对象的16进制的地址
# 如果在自定义的类中实现了object的类魔法方法__str__方法 会返回__str__的字符串
print(xiaoming)


# 自定义一个犬类
class Dog(object):

    def __init__(self):
        self.name = "旺财"

    # 只要执行了 del 对象名 就会走__del__方法
    # 等到对象的引用计数为0 才会执行__del__方法
    # 监听对象销毁
    def __del__(self):
        print("再见")

# 对象
wangcai = Dog()
# python中是自动内存管理
# del wangcai 释放内存

# 提前销毁对象
# del wangcai
#
# input()


# 第二部分
wangcai1 = wangcai
wangcai2 = wangcai

del wangcai
del wangcai1
del wangcai2

input()


# 自定义类 人  名字 年龄 学号
class Person(object):

    # 构造方法
    def __init__(self, name):
        # 添加属性
        self.name = name

    # 打印信息
    def info(self):
        print("姓名:%s" % self.name)

# 小明
xiaoming = Person("小明")
# print(xiaoming)
# print(xiaoming.name)
# print(id(xiaoming.name))
print(id(xiaoming.info))

# 小红
xiaohong = Person("小红")
# print(xiaohong)
# print(xiaohong.name)
# print(id(xiaohong.name))
print(id(xiaohong.info))

# 使用一个类创建出来的对象的属性是需要单独开辟内存
# 使用一个类创建出来的对象 调用这个自定义类的方法其实就是一个(唯一的)
# 如果区分是哪个对象调用的?
# 通过实例方法的第一个参数self 来判断是哪个对象调用的


# 自定义师傅类
# Master 是object的子类 object是Master的父类(相对)
class Master(object):

    # 构造方法
    def __init__(self):
        # 属性
        self.kongfu = "古法煎饼果子配方"

    # 会制作煎饼果子
    def make_cake(self):
        print("按照<%s>制作煎饼果子" % self.kongfu)



# 自定义徒弟类
# Prentice(Master) Prentice是Master的子类 Master 是Prentice 父类(相对)
class Prentice(Master):
    pass
    

# 李师傅对象
lishifu = Master()
print(lishifu.kongfu)
lishifu.make_cake()
print("="*40)

# 大猫
damao = Prentice()
print(damao.kongfu)
damao.make_cake()

# 自定义师傅类
# Master 是object的子类 object是Master的父类(相对)
class Master(object):
    # 构造方法
    def __init__(self):
        print("Master")
        # 属性
        self.kongfu = "古法煎饼果子配方"

    # 会制作煎饼果子
    def make_cake(self):
        print("按照<%s>制作煎饼果子" % self.kongfu)

    # 大烟袋
    def dayandai(self):
        print("大烟袋")


# 自定义新东方
class School(object):
    # 构造方法
    def __init__(self):
        print("School")
        # 属性
        self.kongfu = "现代煎饼果子配方"

    # 会制作煎饼果子
    def make_cake(self):
        print("按照<%s>制作煎饼果子" % self.kongfu)

    # 香烟
    def xiaoyandai(self):
        print("小烟袋")

# 自定义徒弟类
# 大猫-> 会古法(李师傅) 会现代(新东方)
# 自定义一个子类 如果子类继承了多个父类
# 如果多个父类的方法名相同 子类会继承第一个父类方法(规则)
# 如果多个父类的方法名不同 子类可以全部继承
# 如果多个父类的属性名相同 会继承第一个父类的
# 为什么? 是因为子类会继承多个父类(方法名相同__init__)的第一个父类的方法(__init__)
# 注意: __init__负责对象属性的赋值

class Prentice(Master, School):
    pass


# # 大猫
damao = Prentice()
# 属性-继承
print(damao.kongfu)
# 方法-继承
damao.make_cake()
# 大烟袋
damao.dayandai()
# 小烟袋
damao.xiaoyandai()

# 自定义师傅类
# Master 是object的子类 object是Master的父类(相对)
class Master(object):
    # 构造方法
    def __init__(self):
        print("Master")
        # 属性
        self.kongfu = "古法"

    # 会制作煎饼果子
    def make_cake(self):
        print("古法煎饼果子")

# 自定义新东方
class School(object):
    # 构造方法
    def __init__(self):
        print("School")
        # 属性
        self.kongfu = "现代"

    # 会制作煎饼果子
    def make_cake(self):
        print("现代煎饼果子" )


# 自定义徒弟类
# 大猫
# 猫氏煎饼果子配方
# 会制作猫氏煎饼果子
class Prentice(Master, School):

    # 构造方法
    # 重写: 子类继承了父类 子类实现了父类的方法 做自己特有的事情
    def __init__(self):
        print("Prentice")
        self.kongfu = "猫氏"

    # 会制作煎饼果子
    def make_cake(self):
        print("猫氏煎饼果子")


# 总结: 如果子类继承了父类
# 子类重新了父类已有的方法 那么子类将不再使用父类的同名方法 只会使用自己的
# 无论是__init__方法 还是自定义的方法 都不会使用父类的 只会使用自己类内部


# # 大猫
damao = Prentice()
print(damao.kongfu)
# print(damao.kongfu1)
damao.make_cake()

# 自定义师傅类
class Master(object):
    # 构造方法
    def __init__(self):
        print("Master")
        # 属性
        self.kongfu = "古法"

    # 会制作煎饼果子
    def make_cake(self):
        print("古法煎饼果子")

# 自定义新东方
class School(object):
    # 构造方法
    def __init__(self):
        print("School")
        # 属性
        self.kongfu = "现代"

    # 会制作煎饼果子
    def make_cake(self):
        print("现代煎饼果子" )


# 自定义徒弟类
# 大猫
# 猫氏煎饼果子配方
# 会制作猫氏煎饼果子
# 会制作古法煎饼果子
# 会制作现代煎饼果子
class Prentice(Master, School):

    def __init__(self):
        print("Prentice")
        self.kongfu = "猫氏"

    # 会制作煎饼果子
    def make_cake(self):
        print("猫氏煎饼果子")

    # 制作古法
    def make_old_cake(self):
        # 使用父类的方法(因为和子类重名)
        # 解决方法
        # 父类类名.实例方法名(self)
        Master.make_cake(self)

    # 制作现代
    def make_new_cake(self):
        School.make_cake(self)


# # 大猫
damao = Prentice()
print(damao.kongfu)
# 猫氏
damao.make_cake()
# 古法
damao.make_old_cake()
# 现代
damao.make_new_cake()

# 自定义师傅类
class Master(object):
    # 构造方法
    def __init__(self):
        print("Master")
        # 属性
        self.kongfu = "古法"

    # 会制作煎饼果子
    def make_cake(self):
        print("<%s>煎饼果子" % self.kongfu)

# 自定义新东方
class School(object):
    # 构造方法
    def __init__(self):
        print("School")
        # 属性
        self.kongfu = "现代"

    # 会制作煎饼果子
    def make_cake(self):
        print("<%s>煎饼果子" % self.kongfu)


# 自定义徒弟类
# 大猫
# 猫氏煎饼果子配方
# 会制作猫氏煎饼果子
# 会制作古法煎饼果子
# 会制作现代煎饼果子
class Prentice(Master, School):

    def __init__(self):
        print("Prentice")
        self.kongfu = "猫氏"

    # 会制作煎饼果子
    def make_cake(self):
        self.__init__()
        print("<%s>煎饼果子" % self.kongfu)

    # 制作古法
    def make_old_cake(self):
        # 使用父类的方法(因为和子类重名)
        # self.kongfu = "古法"
        Master.__init__(self)
        Master.make_cake(self)



    # 制作现代
    def make_new_cake(self):
        # self.kongfu = "现代
        School.__init__(self)
        School.make_cake(self)


# # 大猫
damao = Prentice()

# 猫氏
damao.make_cake()
# 古法
damao.make_old_cake()
# 现代
damao.make_new_cake()

damao.make_cake()


# 自定义师傅类
class Master(object):
    # 构造方法
    def __init__(self):
        print("Master")
        # 属性
        self.kongfu = "古法"

    # 会制作煎饼果子
    def make_cake(self):
        print("古法煎饼果子")

# 自定义新东方
class School(object):
    # 构造方法
    def __init__(self):
        print("School")
        # 属性
        self.kongfu = "现代"

    # 会制作煎饼果子
    def make_cake(self):
        print("现代煎饼果子" )


# 自定义徒弟类
# 大猫
# 猫氏煎饼果子配方
# 会制作猫氏煎饼果子
# 会制作古法煎饼果子
# 会制作现代煎饼果子
class Prentice(Master, School):

    def __init__(self):
        print("Prentice")
        self.kongfu = "猫氏"

    # 会制作煎饼果子
    def make_cake(self):
        print("猫氏煎饼果子")

    # 制作古法
    def make_old_cake(self):
        # 使用父类的方法(因为和子类重名)
        # 解决方法
        # 错误的方法
        # 跟继承没有任何的关系 需要开辟内存的
        # Master().make_cake()

        # 01:父类类名.实例方法名(self) -> 新式类或者经典类 都可以用
        # Master.make_cake(self)
        # 02: super(子类名, self).实例方法名() -> 适用于新式类
        # super(Prentice, self).make_cake()
        # 03: 对02的简写 super().make_cake()
        super().make_cake()

    # 制作现代
    def make_new_cake(self):
        # School.make_cake(self)
        # super(Prentice, self).make_cake()
        super().make_cake()
        # 在使用super().make_cake() 会打印 古法煎饼果子 多个父类只会调用第一个父类的方法
        # 如果子类继承了多个父类
        # 子类要使用父类的同名方法 可以通过 父类名.方法名
        # 如果是单继承 可以 父类名.方法名 或者super的两种方式都可以的
# # 大猫
damao = Prentice()
print(damao.kongfu)
# # 猫氏
# damao.make_cake()
# # 古法
damao.make_old_cake()
# # 现代
damao.make_new_cake()

# lishifu = Master()
# Master().make_cake()



# 自定义一个类
class Master(object):

    def __init__(self):
        self.kongfu = "古法"
        # 这个属性只想在类里面使用 不可以在类的外面使用
        # python中的私有属性: __私有属性名
        self.__money = 100000


    # 制作煎饼果子
    def make_cake(self):
        print("制作古法煎饼果子")
        # 私有属性可以在类的内部使用
        print(self.__money)
        # 私有的方法可以在类的内部使用
        self.__hello_python()

    # 私有方法
    def __hello_python(self):
        print("你好龟叔")


# lishifu = Master()
# print(lishifu.kongfu)
# 如果一个属性私有后 在类的外面是不可以使用的
# print(lishifu.__money)
# lishifu.make_cake()
# 如果一个方法私有后 在类的外面是不可以调用的
# lishifu.__hello_python()


# 如果有了继承以后
# 徒弟
class Prentice(Master):
    def xx(self):
        print("xx")
        # 不能继承父类的私有属性或者方法
        # self.__money
        # self.__hello_python()

damao = Prentice()
print(damao.kongfu)
# 如果子类继承了父类 但是不能继承父类的私有属性
# print(damao.__money)
damao.make_cake()
# 如果子类继承了父类 但是不能继承父类的私有方法
# damao.__hello_python()

# damao.xx()


