import pymysql


def main():
    """获取用户需要查询的信息，并且显示"""
    # 1. 获取用户需要查询的商品名字
    find_item_name = input("请输入商品名字:")

    # 2. 链接数据库
    conn = pymysql.connect(host='localhost',port=3306,database='jing_dong',user='root',password='mysql',charset='utf8')

    # 3. 获取游标对象
    cursor =  conn.cursor()

    # 4. 组织字符串
    sql = """select * from goods where name="%s";""" % find_item_name
    print(sql)

    # 5. 执行查询语句
    cursor.execute(sql)

    # 6. 显示相应的结果
    print(cursor.fetchall())

    # 7. 关闭
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()


