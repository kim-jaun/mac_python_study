import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                password='mysql', db='test', charset='utf8')
print(conn)
conn.close()