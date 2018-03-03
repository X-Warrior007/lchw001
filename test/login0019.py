#About the gun game


# 自定义枪类
class Gun(object):
    # 构造方法
    def __init__(self, model, damage):
        # 型号
        self.model = model
        # 杀伤力
        self.damage = damage
        # 子弹数量 默认为0
        self.bullet_count = 0

    # 重新str
    def __str__(self):
        return "型号:%s, 杀伤力:%d, 子弹数量:%d" % (
            self.model, self.damage, self.bullet_count
        )

    # 填充子弹
    def add_bullets(self, count):
        # 给self.bullet_count赋值
        self.bullet_count += count
        print("填装子弹完成,子弹数量:%d" % self.bullet_count)


# 测试
def main():
    # 使用枪类创建一把AK47
    ak47 = Gun("AK47", 50)
    print(ak47)
    # 填装子弹
    ak47.add_bullets(10)
    print(ak47)

# 执行函数
main()


# 自定义枪类
class Gun(object):
    # 构造方法
    def __init__(self, model, damage):
        # 型号
        self.model = model
        # 杀伤力
        self.damage = damage
        # 子弹数量 默认为0
        self.bullet_count = 0

    # 重新str
    def __str__(self):
        return "型号:%s, 杀伤力:%d, 子弹数量:%d" % (
            self.model, self.damage, self.bullet_count
        )

    # 填充子弹
    def add_bullets(self, count):
        # 给self.bullet_count赋值
        self.bullet_count += count
        print("填装子弹完成,子弹数量:%d" % self.bullet_count)

    # 发射子弹打土匪
    def shoot(self, enemy):
        # 判断枪是否有子弹
        if self.bullet_count <= 0:
            print("%s 没有子弹 请填装子弹" % self.model)
            return

        # 如果有子弹 要发射子弹
        self.bullet_count -= 1
        # 判断是否打中土匪
        # 如果打中了
        if enemy is not None:
            # 叫土匪受伤
            enemy.hurt(self)

        print("发射了一颗子弹 %s剩余子弹:%d" % (self.model, self.bullet_count))


# 自定义玩家类 为了创建(警察对象 和土匪对象)
class Player(object):
    # 构造方法
    def __init__(self, name, hp=100):
        # 属性赋值
        self.name = name
        self.hp = hp
        # 枪属性
        self.gun = None

    # str
    def __str__(self):
        # 如果土匪的血量小于等于0
        if self.hp <= 0:
            return "%s 已经挂掉了" % self.name
        # 可能是警察 可能是土匪 判断下他是否有枪
        if self.gun is None:
            return "%s[%d] 没有佩戴枪" % (self.name, self.hp)
        # 有枪 有血 -> 警察执行
        return "%s[%d], 枪:{%s}" % (self.name, self.hp, self.gun)

    # 土匪受伤方法
    def hurt(self, enemy_gun):
        # 重新计算土匪的血量
        self.hp -= enemy_gun.damage

        # 判断剩余血量
        # 如果血量 <= 0
        if self.hp <= 0:
            print("%s 已经挂掉了" % self.name)
        else:
            print("%s 被 %s 击中，剩余血量: %d" % (self.name, enemy_gun.model, self.hp))

    # 警察打土匪
    def fire(self, enemy):
        # 判断警察是否有枪
        if self.gun is None:
            print("%s 没有佩戴枪 请佩戴枪" % self.name)
            return

        # 判断枪是否有子弹
        if self.gun.bullet_count <= 0:
            # 自动填充子弹
            self.gun.add_bullets(10)

        print("%s 正在向 %s 开火..." % (self.name, enemy.name))
        # 警察拿着枪射击土匪
        self.gun.shoot(enemy)




# 测试
def main():

    # 警察使用枪打土匪
    # 创建AK47
    ak47 = Gun("AK47", 50)
    # 创建警察
    policeman = Player("警察")
    # 创建土匪
    badman = Player("土匪", 70)

    # 警察向土匪开火
    policeman.fire(badman)

    # 给警察配枪
    policeman.gun = ak47

    # 警察再次向土匪开火
    policeman.fire(badman)

    # 警察再次向土匪开火
    policeman.fire(badman)





# 执行函数
main()
