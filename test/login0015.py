#About print Students Management System


import os
# 保存学生的数据

all_dict = {}
# 定义一个变量 -> 全局变量
file_name = "student.txt"

# 加载文件中的数据
def load_info():
    # 判断文件是否存在
    if not os.path.exists(file_name):
        # 创建一个
        f = open(file_name, "w", encoding="utf-8")
        # 写入数据
        f.write("{}")
        f.close()
    # 读取数据
    f = open(file_name, "r", encoding="utf-8")
    ret = f.read()
    global all_dict
    # 类型转换
    all_dict = eval(ret)
    f.close()

# 打印信息
def print_menu():
    print("---------------------------")
    print("      学生管理系统 V1.0")
    print(" 1:添加学生")
    print(" 2:删除学生")
    print(" 3:修改学生")
    print(" 4:查询学生")
    print(" 5:显示所有学生")
    print(" 6:保存数据")
    print(" 7:退出系统")
    print("---------------------------")
    index = input("请选择:")
    # 判断
    if index.isdigit() and (0 < int(index) < 8):
        return int(index)
    else:
        print("输入错误!!!")
        print_menu()



# 1:添加学生
def add_info():
    my_name = input("请输入您的名字:")
    my_age = input("请输入你的年龄:")
    my_dict = {"name": my_name, "age": my_age}
    # 保存到all_dict中
    all_dict[my_name] = my_dict
    print("保存数据成功...")

# 2:删除学生
def delete_info():
    my_name = input("请输入您的名字:")
    # 判断
    if my_name in all_dict:
        del all_dict[my_name]
        print("删除数据成功...")
    else:
        print("输入的名字有误!!!")

# 3:修改学生
def update():
    my_name = input("请输入您的名字:")
    # 判断
    if my_name in all_dict:
        my_age = input("请输入你的年龄:")
        all_dict[my_name]["age"] = my_age
        print("修改数据成功...")
    else:
        print("输入的名字有误!!!")

# 4:查询学生
def select_info():
    my_name = input("请输入您的名字:")
    if my_name in all_dict:
        print(all_dict[my_name])
    else:
        print("输入的名字有误!!!")

# 5:显示所有学生
def select_all_info():
    print(all_dict)


# 6:保存数据
def save_info():
    f = open(file_name, "w", encoding="utf-8")
    # 写入数据
    f.write(str(all_dict))
    # 关闭文件
    f.close()

# 定义一个函数 来完成系统的运行
def main():
    # 加载文件中的数据
    load_info()
    # 死循环
    while True:
        # 执行打印信息
        index = print_menu()
        if index == 1:
            add_info()
        elif index == 2:
            delete_info()
        elif index == 3:
            update()
        elif index == 4:
            select_info()
        elif index == 5:
            select_all_info()
        elif index == 6:
            save_info()
        elif index == 7:
            print("拜拜")
            break



# 执行
main()


# 如果已经使用文件保存过数据
# 当程序启动 我们需要把文件的数据读取到内存中(all_dict中)
# 因为读取内存的数据快
# all_dict
all_dict = {}
# 01读取文件中的数据
# f = open("hm.txt", "r", encoding="utf-8")
# ret = f.read()
# # 类型转换
# all_dict = eval(ret)
# print(type(all_dict))
# f.close()

# 02 保存内存的数据到文件中
# f = open("hm.txt", "w", encoding="utf-8")
# # 写入数据
# f.write(str(all_dict))
# # 关闭文件
# f.close()
