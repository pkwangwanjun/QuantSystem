# -*- coding: utf-8 -*-
# /root/anaconda3/bin/python
import grpc
import times
from concurrent import futures
from example_signal import data_pb2
from example_signal import data_pb2_grpc
import numpy as np
from collections import deque
import queue
import gc
import threading
import logging
import os
import redis
import opera

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_HOST = '0.0.0.0'
_PORT = '8088'

opera.log_format('signal_logs.log')
redis_pool = redis.ConnectionPool(host='127.0.0.1', port= 6379, password= '5757124', db= 1)
redis_conn = redis.Redis(connection_pool= redis_pool)
# TODO:内存按时清空
# TODO:多client操作
# TODO:落数据库 redis
# TODO:打印日志
# TODO:用户token
 
class FormatData(data_pb2_grpc.FormatDataServicer):
    def DoFormat(self, request, context):
        # index_code,time,price,amount,type
        # consumer_index
        global redis_conn
        direct = request.direct
        index_code = request.index_code
        index_code = 'signal'+':'+times.strftime("%Y%m%d", times.localtime())+':'+index_code
        time = request.time
        price = request.price
        amount = request.amount
        index = request.index
        type = request.type
        if direct == 'push':
            try:
                redis_conn.rpush(index_code,str({'time':time,'price':price,'amount':amount,'index':index,'type':index}))
                logging.info("receive stock data, save it. stock_index:{}".format(index_code))
                return data_pb2.Rlt(direct='push:s',index_code=index_code,time=time,price=price,amount=amount,index=index,type=type)
            except:
                logging.info("receive stock data, can't save it. stock_index:{}".format(index_code))
                return data_pb2.Rlt(direct='push:f',index_code=index_code,time=time,price=price,amount=amount,index=index,type=type)
        elif direct == 'pull':
            if redis_conn.llen(index_code)!=0 and index<=redis_conn.llen(index_code)-1:
                signal = eval(redis_conn.lindex(index_code,index))
                time = signal['time']
                price = signal['price']
                amount = signal['amount']
                logging.info("pull stock data, stock_index:{},index:{}".format(index_code,index))
                return data_pb2.Rlt(direct='pull:s',index_code=index_code[9:],time=time,price=price,amount=amount,index=index,type=type)
            else:
                return data_pb2.Rlt(direct='pull:no data',index_code=index_code[9:],time=time,price=price,amount=amount,index=index,type=type)
        else:
            pass




def serve():
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    #grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=1),options=(('grpc.so_reuseport', 0),))
    data_pb2_grpc.add_FormatDataServicer_to_server(FormatData(), grpcServer)
    grpcServer.add_insecure_port(_HOST + ':' + _PORT)
    grpcServer.start()
    try:
        while True:
            logging.info('time:{} server start'.format(times.strftime("%Y-%m-%d %H:%M:%S", times.localtime())))
            #print('time:{} server'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        grpcServer.stop(0)

if __name__ == '__main__':
    t = threading.Thread(target=opera.collect_on_time, name='collect_gc')
    t.start()
    serve()
    
