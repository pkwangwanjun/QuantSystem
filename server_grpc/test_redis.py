import pandas as pd
import numpy as np
import redis

redis_pool = redis.ConnectionPool(host='127.0.0.1', port= 6379, password= '5757124', db= 0)
redis_conn = redis.Redis(connection_pool= redis_pool)
# 增加列表，往左边增加
v = redis_conn.lpush('000725.SZ', 1,2,3,4,5)

redis_conn.rpush('000725.SZ', 1,2,3,4,5)
redis_conn.rpush('000725.SZ', 6)
# 最左边增加一个
v = redis_conn.lpush('000725.SZ', 6)
# 查看列表长度
v = redis_conn.llen('000725.SZ')
# 根据索引获取列表值
redis_conn.lindex('000725.SZ', 2)
# 获取一段数据
v = redis_conn.lrange('000725.SZ', 2, 5)
# 删除左边的值
v = redis_conn.lpop('000725.SZ')

# 持久化配置
# 1.过程中自动持久化 2. 每天行情结束手动持久化

import redis
rdb = redis.Redis(host='127.0.0.1', port=6379, db=0, password='5757124')

# 持久化数据
#rdb.save()
# 删除db中的数据
rdb.flushdb()

#redis_conn.rpush('000725.SZ', 1,2,3,4,5)
#redis_conn.rpush('000725.SZ', 6)
#redis_conn.lindex('000725.SZ', 2)

redis_conn.rpush('000001.SZ',str({'index_code':1,'time':1,'price':1,'amount':1,'type':1}))

if __name__=='__main__':
    pass