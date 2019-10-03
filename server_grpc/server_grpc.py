# -*- coding: utf-8 -*-
# /root/anaconda3/bin/python
import grpc
import time
from concurrent import futures
from example import data_pb2
from example import data_pb2_grpc
import numpy as np
from collections import deque
import queue
import gc
import threading
import logging
import os

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_HOST = '0.0.0.0'
#_HOST = '127.0.0.1'
_PORT = '8088'

#stock_signal = {}
stock_signal = queue.Queue(3000)
client_consume_index = {}
# TODO:内存按时清空
# TODO:多client操作
# TODO:落数据库
# TODO:打印日志
 
fmt = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s'
filename = os.path.join(os.getcwd(),'server_logs.log')
logging.basicConfig(level=logging.DEBUG,
                    format=fmt,
                    filename=filename,
                    filemode='w',
                    datefmt='%a, %d %b %Y %H:%M:%S'
                    )


def collect_on_time():
    while True:
        time_now = time.strftime("%H:%M:%S", time.localtime())
        
        if time_now>='16:00:00' and time_now<='16:01:00' :
            global stock_signal
            stock_signal.queue.clear()
            time.sleep(50)
            gc.collect()
            logging.info('time:{} collect done'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
            #print('time:{} collect done'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))



class FormatData(data_pb2_grpc.FormatDataServicer):
    def DoFormat(self, request, context):
        # index_code,time,price,amount,type
        direct = request.direct
        index_code = request.index_code
        time = request.time
        price = request.price
        amount = request.amount
        type = request.type
        global stock_signal
        if direct == 'push':
            stock_signal.put({'index_code':index_code,'time':time,'price':price,'amount':amount,'type':type})
            logging.info("receive stock signal, save it. stock_index:{}".format(index_code))
            #print("receive stock signal, save it")
            return data_pb2.Rlt(direct=direct,index_code=index_code,time=time,price=price,amount=amount,type=type)
        elif direct == 'pull':
            if not stock_signal.empty():
                #print("pull stock signal,remove it")
                signal = stock_signal.get()
                index_code = signal['index_code']
                time = signal['time']
                price = signal['price']
                amount = signal['amount']
                type = signal['type']
                logging.info("pull stock signal,remove it. stock_index:{}".format(index_code))
                return data_pb2.Rlt(direct=direct,index_code=index_code,time=time,price=price,amount=amount,type=type)
            else:
                return data_pb2.Rlt(direct='no data',index_code='',time='',price=float(0),amount=0,type=0)
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
            logging.info('time:{} server start'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
            #print('time:{} server'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        grpcServer.stop(0)

if __name__ == '__main__':
    t = threading.Thread(target=collect_on_time, name='collect_gc')
    t.start()
    serve()
    
