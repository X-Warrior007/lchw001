#About algorithm of taking the subway

# 轨道交通价格调整为：
# 6公里(含)内3元;
# 6公里至12公里(含)4元;
# 12公里至22公里(含)5元;
# 22公里至32公里(含)6元;
# 32公里以上部分，每增加1元可乘坐20公里。
# 使用市政交通一卡通刷卡乘坐轨道交通，
# 每自然月内每张卡支出累计满100元以后的乘次，价格给予8折优惠;
# 满150元以后的乘次，价格给予5折优惠;
# 支出累计达到400元以后的乘次，不再享受打折优惠。

# 定义一个变量 记录小明乘坐地铁的距离
km = 90
# 定义一个变量记录单程的价格
every_money = 0
# pass 是一个占位 防止代码报错
# 32公里以上部分，每增加1元可乘坐20公里。
if km > 32:
    # 假设 33公里 -> 6 + 1
    # 假设 52公里 -> 6 + 1
    # 假设 53(32 + 20 + 1)公里 -> 6 + 1 + 1
    # 假设 51(32 +19)公里 -> 6 + 1

    # 计算出超出的部分
    temp_km = km - 32
    # 判断到底整除(取余20)
    if temp_km % 20 == 0:
        every_money = 6 + int(temp_km/20)
    else:
        every_money = 6 + int(temp_km/20) + 1

# 22公里至32公里(含)6元;
elif km > 22:
    every_money = 6
# 12公里至22公里(含)5元;
elif km > 12:
    every_money = 5
# 6公里至12公里(含)4元;
elif km > 6:
    every_money = 4
# 6公里(含)内3元;
else:
    every_money = 3

print("单程票价:%d" % every_money)

# 小明都需要上20天班，每次上班需要来回1次，即每天需要乘坐2次同样路线的地铁
# 出行40次
# 每自然月内每张卡支出累计满100元以后的乘次，价格给予8折优惠;
# 满150元以后的乘次，价格给予5折优惠;
# 支出累计达到400元以后的乘次，不再享受打折优惠。

# 定义一个变量 记录小明这个月花的总钱数
total_money = 0
# 记录次数
i = 1
while i <= 40:
    # [0,100)
    if total_money < 100:
        total_money += every_money
    # [100,150)
    elif total_money >= 100 and total_money < 150:
        total_money += every_money * 0.8
    # [150, 400)
    elif total_money >= 150 and total_money < 400:
        total_money += every_money * 0.5
    else:
        total_money += every_money
    i += 1

print("小明乘坐地铁总的消费:%f" % total_money)
