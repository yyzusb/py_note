#encoding=utf-8

#链接redis
import redis

if __name__ == '__main__':
    #在链接或者读取外界文件的时候，要try一下
    try:
        rs = redis.Redis(host="192.168.121.6",port=6379,db=0)
        rs.set('foo','bar')
    except Exception as e:
        print(e)
    else:
        rs_value = rs.get('foo')
        print(rs_value)
