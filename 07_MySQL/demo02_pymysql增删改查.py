#1、导入pymysql包
import pymysql

if __name__ == '__main__':
    #2、创建连接对象,cursor用来执行sql，conn用来提交sql到服务器
    conn  =  pymysql.connect(host="192.168.30.149",
                             port=3306,
                             user="root",
                             password="1$*k}(=*wg2",
                             database="python",
                             charset="utf8")
    #3、获取游标
    cursor = conn.cursor()
    sql = 'insert into python_user_info (name,age,sex) values ("jack",34,"男")'
    try:
        cursor.execute(sql)
        #4、如果执行成功没有任何反应，可以进行提交
        conn.commit()
        print('Sql执行成功')
    except Exception as result:
        print(result)
        # 如果失败进行事务回滚，指在InnoDB引擎上
        conn.rollback()
        print('Sql执行失败,已经回滚')

    #5、执行sql语句
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



