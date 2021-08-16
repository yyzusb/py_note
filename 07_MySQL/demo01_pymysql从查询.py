#1、导入pymysql包
import pymysql

if __name__ == '__main__':
    #2、创建连接对象
    conn  =  pymysql.connect(host="192.168.30.149",
                             port=3306,
                             user="root",
                             password="1$*k}(=*wg2",
                             database="python",
                             charset="utf8")
    #3、获取游标
    cursor = conn.cursor()

    #4、执行sql语句
    sql = 'select * from python_user_info'
    cursor.execute(sql)

    #5、显示结果
    result =  cursor.fetchall()
    for line in (result):
        print(line)

    #6、关闭游标
    cursor.close()
    #7、关闭连接
    conn.close()



