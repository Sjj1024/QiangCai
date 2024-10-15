import os
import threading
import time
import uiautomator2 as u2


# 连接手机
def connect_phone(device_name):
    d = u2.connect(device_name)
    if not d.uiautomator.start():
        # 启动uiautomator服务
        print("start uiautomator")
        d.uiautomator.start()
        time.sleep(2)
    return d


def open_feishu(device_name):
    d = connect_phone(device_name)
    print("打开飞书")
    d.app_start("com.ss.android.lark")
    time.sleep(30)
    # 打开闹钟
    print("打开闹钟")
    d.app_start("com.sec.android.app.clockpackage")


def run(device_name):
    print("运行程序")
    while True:
        try:
            open_feishu(device_name)
        except Exception as e:
            print(e)
            time.sleep(5)


if __name__ == '__main__':
    # 这是叮咚抢菜，此处填设备编号
    device_name = "b8c282ac"
    run(device_name)
