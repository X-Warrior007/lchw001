class Person(object):
    def __init__(self, age):
        self.__age = age


laowang = Person(48)
print(laowang.__age)
