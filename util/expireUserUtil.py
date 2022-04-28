import pymysql


def getExpireUser(db):
    # 打开数据库连接
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='123456',
                         database=db)

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = """SELECT email
       FROM `user`
       where class_expire < date(now())"""

    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()

    user = []
    for i in results:
        user.append(i[0])

    return user


if __name__ == '__main__':
    db = "oneky"
    user = getExpireUser(db)
    expireUser = []
    url = "../data/" + db + "Expire.txt"
    for i in set(user):
        expireUser.append(i + ',' + "\n")
    f = open(url, "w")
    f.writelines(set(expireUser))
    f.close()
    print("过期用户：" + str(len(set(expireUser))) + " - " + str(set(expireUser)))