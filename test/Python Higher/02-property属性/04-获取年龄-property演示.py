class Person(object):
    def __init__(self, age):
        self.__age = age
        self.num = 100  # 这是一个普通的属性，这个属性可以通过 对象.num直接操作，这种方式容易产生一些问题，例如类型不对

    @property
    def age(self):
        print("这里是获取数值权限的验证")
        if 1==1:
            return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age

laowang = Person(48)
# print(laowang.__age)
# print(laowang.get_age())
# laowang.set_age(49)
# print(laowang.get_age())

# 当有了property属性以后，就可以做到，在操作的时候 像是操作的普通的属性，但是真的过程是调用对应的方法
# 只要在方法中实现相应的功能，就能够做到一些权限以及数据类型的验证等功能

# 通俗的说：property属性要比普通属性强，它多一个函数的执行，在函数中可以完成很多的功能的实现

print(laowang.age)
laowang.age = 50
print(laowang.age)
