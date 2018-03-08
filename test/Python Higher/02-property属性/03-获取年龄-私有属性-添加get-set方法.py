class Person(object):
    def __init__(self, age):
        self.__age = age

    def get_age(self):
        print("这里是获取数值权限的验证")
        if 1==1:
            return self.__age

    def set_age(self, new_age):
        print("这里是设置数值权限的验证")
        if 1==1:
            self.__age = new_age


laowang = Person(48)
# print(laowang.__age)
print(laowang.get_age())
laowang.set_age(49)
print(laowang.get_age())
