from controller.flow_controller import FlowController


def auto_send(is_run_history, *args):
    ss = FlowController(*args)
    if is_run_history:
        ss.start()

if __name__ == '__main__':
    # 默认只处理当天数据
    auto_send(is_run_history=False)