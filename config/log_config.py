import os
from datetime import date, datetime

class LogPath:
    today = date.today()
    now = datetime.now()
    today_time = now.strftime("%Y-%m-%d %H:%M")
    # 写入地址
    write_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "log")
    # 日志目录
    logs_file_path = os.path.join(write_path, "{}".format(today))
    logs_path = os.path.join(logs_file_path, "auto_{}.log".format(today_time))