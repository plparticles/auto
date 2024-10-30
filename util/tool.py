import time
from util.log import Logs
from configparser import ConfigParser

logger = Logs("处理时间").get_logger()

def log_time(fun):
    def func(*args, **kwargs):
        start_time = time.time()
        result = fun(*args, **kwargs)
        end_time = time.time()
        logger.info("method:{}，执行耗时:{}".format(fun.__name__, end_time - start_time))
        return result

    return func


def read_config(file):
    config = ConfigParser()
    # 读取INI文件
    config.read(file)
    return config