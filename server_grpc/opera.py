import gc
import threading
import logging
import os
import time

def log_format(log_file):
    fmt = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s'
    filename = os.path.join(os.getcwd(),log_file)
    logging.basicConfig(level=logging.DEBUG,
                        format=fmt,
                        filename=filename,
                        filemode='w',
                        datefmt='%a, %d %b %Y %H:%M:%S'
                        )


def collect_on_time():
    while True:
        time_now = time.strftime("%H:%M:%S", time.localtime())
        if time_now>='16:00:00' and time_now<='16:01:00':
            rdb.save()
            rdb.flushdb()
            time.sleep(60)
            gc.collect()
            logging.info('time:{} collect done'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        time.sleep(30)