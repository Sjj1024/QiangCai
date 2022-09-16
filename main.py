from src.dingdong import run as dingdong_run
from src.meituan import run as meituan_run
from src.meituan_maicai import run as maicai_run


def run(device_name):
    print("""
    1：开始叮咚抢菜
    2：开始美团APP抢菜(在美团APP首页进入抢菜页面开始抢菜)
    3：开始美团买菜APP抢菜(单独的美团买菜APP中开始抢菜)""")
    input_str = input("请输入编号：")
    if input_str == "1":
        print("开始执行叮咚抢菜程序.....")
        dingdong_run(device_name)
    elif input_str == "2":
        print("开始执行美团抢菜程序.....")
        meituan_run(device_name)
    elif input_str == "3":
        print("开始执行美团抢菜APP抢菜程序.....")
        maicai_run(device_name)

if __name__ == '__main__':
    # 修改为设备编码
    device_name = "RFCN309ABWX"
    run(device_name)