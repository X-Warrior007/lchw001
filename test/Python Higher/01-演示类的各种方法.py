class Family(object):

    # 定一个类属性，用来存储苹果的个数
    num = 5

    def __init__(self, name):
        # 定义一个实例属性，用来存储姓名
        self.name = name

    @classmethod
    def eat_apple(cls):
        # 需要操作类属性num的值
        cls.num -= 1

    @staticmethod
    def rule():
        print("------约法三章----")
        print("1: 孝敬父母")


# 总结：
# 1. 如果一个实例对象需要一个变量，这个变量的数据是自己独有的，那么一定是实例属性
# 2. 如果N个实例对象需要一些公用的数据，那么就把这个数据存放在类对象中的变量中，即类属性
# 3. 默认需要传递 实例对象引用的方法，用实例方法
# 4. 默认需要传似 类对象引用的方法，用类方法
# 5. 默认不需要 实例对象/类对象 引用的方法, 用静态方法
# 实际开发是，到底用什么方法，根据需求来确定

son1 = Family("老大")
son2 = Family("小弟")

print(Family.num)
son1.eat_apple()
son2.eat_apple()
print(Family.num)

Family.rule()
