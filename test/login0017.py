#About the second  adding of class


class Person(object):

    def __init__(self):
        self.name = "老王"
        self.__age = 20

    # 对私有属性取值
    def get_age(self):
        return self.__age

    # 对私有属性赋值
    def set_age(self, new_age):
        self.__age = new_age


p = Person()
# 取值
# print(p.name)
# 赋值
# p.name = "老王往"
# 取值
# print(p.name)

# 如果想在类的外面使用对象对私有属性进行取值和赋值操作
# 对私有属性进行取值
print(p.get_age())
# 赋值
p.set_age(200)
# 取值
print(p.get_age())



# def my_func(a):
#     ret =  a - a
#     print(a)
#
#
# my_func(10)
# my_func("hello")

# 自定义一个犬类
class Dog(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("啃骨头")

# 自定义一个人类
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("肯德基")

# 定义一个狗
wangcai = Dog("旺财", 5)
# print(wangcai.name, wangcai.age)
# wangcai.eat()

# 定义一个人
xiaoming = Person("小明", 20)
# print(xiaoming.name, xiaoming.age)
# xiaoming.eat()

# 定义一个函数
def print_info(object):
    print(object.name, object.age)
    object.eat()

print_info(wangcai)
print_info(xiaoming)


# 自定义一个人类(服务于中国人)
class Person(object):

    # 类属性
    # 定义在类的里面 方法的外面的变量 叫做类属性
    num = 100
    # 国籍
    country = "中国国"

    # def __init__(self, name, age, country="中国"):
    #     self.name = name
    #     self.age = age
    #     self.country = country

    def __init__(self, name, age):
        self.name = name
        self.age = age



p1 = Person("小明", 22)
print(p1.country)
p2 = Person("小红", 22)
print(p2.country)


# 如果想使用类属性(get)
# 格式: 类名(类对象).类属性
# print(Person.num)
# 如果想设置类属性的值(set)
# 格式:类名(类对象).类属性 = 值
# Person.num = 200
# print(Person.num)

# 如果想使用类属性(get)
# 类名(类对象)创建出来的对象 叫做实例对象
# 格式:实例对象.类属性
# p = Person("小明", 22)
# print(p.num)

# 如果想设置类属性的值(set) 不可以通过对象完成
# print(Person.num)
# p = Person("小明", 22)
# print(p.num)
# 如果使用实例对象.类属性名(添加了一个实例属性(和类属性名相同))
# p.num = 300
# print(p.num)
# print(Person.num)

"""
如果获取类属性
    格式: 类名(类对象).类属性名 实例对象.类属性名
如果设置类属性的值
    格式: 类名(类对象).类属性名 = 值
"""

#
# 查看类属性
# print(id(Person.num))
#
# print(id(Person("小明", 22).num))
#
# print(id(Person("小明", 23).num))


# 类属性只会开辟一份内存空间 每个类的类属性的地址是唯一的

# print(Person.num)
# Person.num = 200
# print(Person("小明", 22).num)
#
# print(Person("小明", 23).num)

# 自定义一个人类(服务于中国人)
class Person(object):

    # 类属性
    # 定义在类的里面 方法的外面的变量 叫做类属性
    num = 100
    # 国籍
    country = "中国国"

    # def __init__(self, name, age, country="中国"):
    #     self.name = name
    #     self.age = age
    #     self.country = country

    def __init__(self, name, age):
        self.name = name
        self.age = age



p1 = Person("小明", 22)
print(p1.country)
p2 = Person("小红", 22)
print(p2.country)


# 如果想使用类属性(get)
# 格式: 类名(类对象).类属性
# print(Person.num)
# 如果想设置类属性的值(set)
# 格式:类名(类对象).类属性 = 值
# Person.num = 200
# print(Person.num)

# 如果想使用类属性(get)
# 类名(类对象)创建出来的对象 叫做实例对象
# 格式:实例对象.类属性
# p = Person("小明", 22)
# print(p.num)

# 如果想设置类属性的值(set) 不可以通过对象完成
# print(Person.num)
# p = Person("小明", 22)
# print(p.num)
# 如果使用实例对象.类属性名(添加了一个实例属性(和类属性名相同))
# p.num = 300
# print(p.num)
# print(Person.num)

"""
如果获取类属性
    格式: 类名(类对象).类属性名 实例对象.类属性名
如果设置类属性的值
    格式: 类名(类对象).类属性名 = 值
"""

#
# 查看类属性
# print(id(Person.num))
#
# print(id(Person("小明", 22).num))
#
# print(id(Person("小明", 23).num))


# 类属性只会开辟一份内存空间 每个类的类属性的地址是唯一的

# print(Person.num)
# Person.num = 200
# print(Person("小明", 22).num)
#
# print(Person("小明", 23).num)


class Person(object):
    # 类属性中国国籍
    country = "中国"
    # 私有的类属性
    __hello = "哈喽"

    # 类方法
    # 修饰器
    # 获取
    @classmethod
    def get_hello(cls):
        return cls.__hello

    # 修改
    @classmethod
    def set_hello(cls, new_hello):
        cls.__hello = new_hello


# 想在类的外面 获取类属性的值 修改类属性
# 使用类对象完成对象
# 格式: 类对象(类名).类方法名
# # 获取
# print(Person.get_hello())
# # 修改
# Person.set_hello("hello")
# # 获取
# print(Person.get_hello())


# 实例对象
# 如果通过类方法获取私有的类属性 或者通过类方法设置私有的类属性 也可以通过实例对象调用类方法完成
p = Person()
# 获取
print(p.get_hello())
# 赋值
p.set_hello("hello")
# 获取
print(p.get_hello())


class Person(object):
    __country = "中国"

    def __init__(self):
        self.__age = 10

    # 实例方法(对象方法)
    def get_age(self):
        return self.__age

    # 类方法
    @classmethod
    def get_country(cls):
        return cls.__country

    # 静态方法
    @staticmethod
    def hello():
        print("今天很冷")

# 如果在类的外面调用类中的静态方法
# 类名.静态方法名
# Person.hello()
# 实例对象.静态方法
# p = Person()
# p.hello()

"""
类中有几种类型方法:
    实例方法(对象方法):
        如果在类的内部想使用self
        格式: def 方法名(self):
                   代码逻辑
    类方法:
        如果想在类的内部使用cls
        格式: @classmethod
              def 方法名(cls):
                  代码逻辑
    静态方法:
        如果不使用self 也不使用cls 就可以使用静态方法
        格式: @staticmethod
              def 方法名():
                  代码逻辑
"""


class Person(object):

    # 监听类对象(Person)使用其类创建一个实例对象(xiaoming)的过程
    def __new__(cls, *args, **kwargs):
        print("new")
        return object.__new__(cls)

    # 构造方法
    # 监听python给我创建了一个对象(已经创建完成)
    # 当执行init方法的时候对象已经创建成功
    def __init__(self, name):
        print("init")
        self.name = name

    # 打印对象的属性信息 方便开发
    # def __str__(self):
    #     return ""

    # 监听当对象的引用计数为0的时候 python会执行del方法
    def __del__(self):
        print("再见")

xiaoming = Person("小明")
print(xiaoming)

   
