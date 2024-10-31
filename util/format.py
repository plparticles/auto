

def get_half_hour_indices(time_period):
        # 将时间段拆分为开始时间和结束时间
        start_time, end_time = time_period.split('-')

        # 将时间字符串转换为小时和分钟
        start_hour, start_minute = map(int, start_time.split(':'))
        end_hour, end_minute = map(int, end_time.split(':'))

        # 计算开始时间和结束时间对应的半小时下标
        start_index = start_hour * 2 + (start_minute // 30)
        end_index = end_hour * 2 + (end_minute // 30)

        # 生成从开始下标到结束下标的列表
        indices = list(range(start_index + 1, end_index + 1))

        return indices

if __name__ == '__main__':
    time_period = "1:00-1:30"
    indices = get_half_hour_indices(time_period)
    print(indices)