# -*- coding: utf-8 -*-
import grpc
import time
from concurrent import futures
from example import data_pb2, data_pb2_grpc
import numpy as np
from collections import deque

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_HOST = '127.0.0.1'
_PORT = '8088'

stock_signal = {}

class FormatData(data_pb2_grpc.FormatDataServicer):
    def DoFormat(self, request, context):
        index_code = request.index_code
        action = request.action
        value = request.value
        global stock_signal
        if index_code not in stock_signal:
            stock_signal[index_code] = deque()
        else:
            stock_signal[index_code].appendleft({'action':action,'value':value})
        print("receive stock signal, save it")
        return data_pb2.Rlt(index_code=index_code,action=action,value=value)

def serve():
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    data_pb2_grpc.add_FormatDataServicer_to_server(FormatData(), grpcServer)
    grpcServer.add_insecure_port(_HOST + ':' + _PORT)
    grpcServer.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        grpcServer.stop(0)

if __name__ == '__main__':
    serve()
