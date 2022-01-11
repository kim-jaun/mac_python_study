import pymysql
try:
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                    password='mysql', db='test', charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select * from dept order by deptno")
    data = cursor.fetchall()
    for i in data:
        print(i)
except Exception as ex:
    print('에러', ex)
finally:
    conn.close()