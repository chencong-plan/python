import pymysql

# 连接数据库
connect = pymysql.Connect(
    host='120.76.142.232',
    port=3306,
    user='chencong',
    passwd='123456',
    db='cmall',
    charset='utf8'
)

# 获取游标
cursor = connect.cursor()

# 插入数据
sql = "INSERT INTO cmall_user(username,password,nickname,email) VALUES('%s','%s','%s','%s')"
data = ('chencong', '123456', '聪聪不匆匆', '123@qq.com')
cursor.execute(sql % data)
connect.commit()
print('成功插入', cursor.rowcount, '条数数据')

# 修改数据
sql = "UPDATE cmall_user SET username = '%s' WHERE email = '%s'"
data = ('congcong', '123@qq.com')
cursor.execute(sql % data)
connect.commit()
print("成功修改", cursor.rowcount, "条数据")

# 删除数据
sql = "DELETE FROM cmall_user WHERE username = '%s'"
data = 'congcong'
cursor.execute(sql % data)
connect.commit()
print("成功删除", cursor.rowcount, "条数据")

# 查询
# sql = "select id,username,password,nickname,email from cmall_user where username = '%s'"
# data=('congcong')
# cursor.execute(sql % data)
sql = "SELECT id,username,password,nickname,email FROM cmall_user"
cursor.execute(sql)
for row in cursor.fetchall():
    print("id:%d \tusername:%s \tpassword:%s \tnickname:%s \temail:%s" % row)
print("共查出", cursor.rowcount, "条数据")

# 事务处理
sql_1 = "UPDATE cmall_user SET password = 'chencong' WHERE username = 'chencong' "
sql_2 = "UPDATE cmall_user SET password = 'admin' WHERE username = 'admin' "

try:
    cursor.execute(sql_1)
    cursor.execute(sql_2)
except Exception as e:
    connect.rollback()  # 事务回滚
    print("事务处理失败", e)
else:
    connect.commit()  # 提交事务
    print("事务处理成功", cursor.rowcount, "条受影响")

# 关闭连接
cursor.close()
connect.close()
print("关闭数据库连接")
