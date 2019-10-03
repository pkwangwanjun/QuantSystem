#! /usr/bin/env python
# -*- coding: utf-8 -*-
import grpc
import sys
from example import data_pb2
from example import data_pb2_grpc
import threading
import time
import numpy as np

#_HOST = '127.0.0.1'
_HOST = '111.231.144.192'
_PORT = '8088'
MAX_MESSAGE_LENGTH = 10 * 1024 * 1024

class client(object):
    def __init__(self):
        pass

    def run(self,signal):
        conn = grpc.insecure_channel(_HOST + ':' + _PORT, options=[('grpc.max_send_message_length', MAX_MESSAGE_LENGTH), (
                'grpc.max_receive_message_length', MAX_MESSAGE_LENGTH
            )])
        # index_code,time,price,amount,type
        direct = signal['direct']
        index_code = signal['index_code']
        time = signal['time']
        price = signal['price']
        amount = signal['amount']
        type = signal['type']
        client = data_pb2_grpc.FormatDataStub(channel=conn)
        response = client.DoFormat(data_pb2.Stock(direct=direct,index_code=index_code,time=time,price=price,amount=amount,type=type))
        print('direct:{},index_code:{},time:{},price:{},amount:{},type:{}'.format(response.direct,response.index_code,response.time, \
              response.price,response.amount,response.type))

    def test(self,epochs):
        for i in range(epochs):
            direct = 'push'
            index_code = str(np.random.randint(1,100))
            time = str(np.random.randint(1,100))
            price = float(np.random.randint(1,100))
            amount = int(np.random.randint(1,100))
            type = int(np.random.randint(0,3))
            signal = {'direct':direct,'index_code':index_code,'time':time,'price':price,'amount':amount,'type':type}
            self.run(signal)
        print('test done')

if __name__ == '__main__':
    '''
    list = []
    for i in range(6):
        t =threading.Thread(target=run,args=())
        list.append(t)
        t.start()

    for threadinglist in list:
        threadinglist.join()
    '''
    obj=client()
    obj.test(100)
