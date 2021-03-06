# encoding=utf-8
import redis
from rediscluster import RedisCluster

if __name__ == '__main__':
    nodes = [{"host": "192.168.121.6", "port": "7001"},
             {"host": "192.168.121.6", "port": "7002"},
             {"host": "192.168.121.6", "port": "6379"}
             ]

    try:
        str = RedisCluster(startup_nodes=nodes)
    except Exception as e:
        print(e)
