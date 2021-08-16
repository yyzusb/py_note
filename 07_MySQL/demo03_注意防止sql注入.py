'''
最后一节mysql事务笔记放在这里

mysql事务，即原子性，一致性，隔离性 ，持久性。一条sql语句执行的结果中途不可中断，结果必须要一致，正确，不能一边修改后，另一边没有变化，隔离性是sql执行
完成以前结果不会显示出来，执行完毕后才能知道成功与否，持久性修改后永久生效。目前innodb搜索引擎支持事务，MyISAM引擎不支持事物回滚，优点是检索快，适合对
事务没有要求，或者以select，insert为主来创建的表格

索引，索引像书的目录，可以更快查找数据的位置，当表格数据量大时，可以为表格添加索引，增加检索速度，默认情况下，主键也会自动创建索引。经常更新的表不要创建
索引，经常查找的表创建索引，数据量小不用创建索引

联合索引，索引创建成功后生成一个文件 ，创建联合索引可以节省磁盘空间，联合索引要遵守最左原则，即最左边的索引必须是查询条件
'''



import pymysql

if __name__ == '__main__':
    conn =  pymysql.connect(host="192.168.30.149",
                            port=3306,
                            user="root",
                            password="1$*k}(=*wg2",
                            database="python",
                            charset="utf8")

    cursor = conn.cursor()
    #参数用%s代替,参数写道 cursor.execute函数里面
    sql = 'insert into python_user_info (name,age,sex) values (%s,%s,%s)'
    try:
        cursor.execute(sql,('lily',23,'女'))
        #注意提交
        conn.commit()
        print('sql执行成功')
        result = cursor.fetchall()
        for line in (result):
            print(line)
    except Exception  as e:
        print(e)
        #如果失败进行事务回滚，指在InnoDB引擎上
        conn.rollback()
        print('sql执行失败，已经回滚')

    sql = 'select * from python_user_info where %s < %s'
    try:
        cursor.execute(sql,('id',9000))
        conn.commit()
        print('sql执行成功')
        result = cursor.fetchall()
        for line in (result):
            print(line)
    except Exception  as e:
        print(e)
        conn.rollback()
        print('sql执行失败，已经回滚')
    finally:
        cursor.close()
        conn.close()

