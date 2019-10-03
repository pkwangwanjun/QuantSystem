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
    def __init__(self,index_code,index=0):
        self.index_code = index_code
        self.index = index

    def pull(self):
        conn = grpc.insecure_channel(_HOST + ':' + _PORT, options=[('grpc.max_send_message_length', MAX_MESSAGE_LENGTH), (
                'grpc.max_receive_message_length', MAX_MESSAGE_LENGTH
            )])
        # direct,index_code,time,price,amount,index
        direct = 'pull'
        index_code = self.index_code
        time = ''
        price = float(0)
        amount = 0
        index = self.index
        type = 0
        client = data_pb2_grpc.FormatDataStub(channel=conn)
        response = client.DoFormat(data_pb2.Stock(direct=direct,index_code=index_code,time=time,price=price,amount=amount,index=index,type=type))
        if response.direct=='pull:s':
            print('direct:{},index_code:{},time:{},price:{},amount:{},index:{},type:{}'.format(response.direct,response.index_code,response.time, \
                response.price,response.amount,response.index,response.type))
            self.index +=1
        elif response.direct=='pull:f':
            print('no data')
        else:
            pass


if __name__ == '__main__':
    obj=client('000745.SZ',index=0)
    while True:
        obj.pull()
        time.sleep(0.1)
