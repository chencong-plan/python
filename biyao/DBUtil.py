import pymysql

# 连接数据库
connect = pymysql.Connect(
    host='120.76.142.232',
    port=3306,
    user='chencong',
    passwd='123456',
    db='biyao_data',
    charset='utf8'
)

# 获取游标
cursor = connect.cursor()


def execute(sql, params):
    cursor.execute(sql % params)
    connect.commit()
