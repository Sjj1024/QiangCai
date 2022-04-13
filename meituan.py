import os
import platform
import time
import threading
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


def play_voice(content):
    """
    播放声音提醒
    """
    from playsound import playsound
    root_path = os.getcwd()
    video_path = os.path.join(root_path, "sources", "videos", f"{content}.mp3")
    threading.Thread(target=playsound, args=(video_path,)).start()

def qiang_cai(device_name):
    d = connect_phone(device_name)
    d.app_start("com.sankuai.meituan")
    count = 1
    time_start = time.time()
    while True:
        start = time.time()
        if d(textContains="结算(").exists:
            print("点击结算")
            d(textContains="结算(").click()
        else:
            print("点击全选")
            if d(text="全选").exists:
                print("点击全选")
                d(text="全选").click()

        if d(text="我知道了").exists:
            print("点击我知道了")
            d(text="我知道了").click()

        if d(text="重新加载").exists:
            print("重新加载")
            d(text="重新加载").click()

        if d(text="返回购物车").exists:
            print("点击返回购物车")
            d(text="返回购物车").click()

        if d(text="立即支付").exists:
            print("点击立即支付")
            play_voice("success")
            d(text="立即支付").click()

        if d(text="确认并支付").exists:
            print("点击确认并支付")
            play_voice("success")
            d(text="确认并支付").click()

        if d(textContains="极速支付").exists:
            print("极速支付")
            play_voice("success")
            break

        if d(textContains="普通支付").exists:
            print("普通支付")
            play_voice("success")
            break

        if d(resourceId="btn-line").exists:
            play_voice("success")
            print("确认支付")
            d(resourceId="btn-line").click()
            break
        print("本次花费时间:", time.time() - start)
        print("总共花费时间:", (time.time() - time_start) / 60, "分钟，第", count, "次")
        count += 1


def is_mac():
    system = platform.system()
    if system == "Windows":
        print("当前系统是Windows")
        return False
    else:
        print("当前系统是Mac")
        return True


def get_device_list():
    root_path = os.getcwd()
    if is_mac():
        cmd = os.path.join(root_path, "sources", "mac_tools", "adb devices")
    else:
        cmd = os.path.join(root_path, "sources", "win_tools", "adb.exe devices")
    res = os.popen(cmd).read()
    print(f"adb 命令结果是:\n{res}")
    list_phone = [i for i in res.split("\n") if i]
    if len(list_phone) > 1:
        phone_num = [i.split("\t")[0] for i in list_phone[1:] if i]
        print(f"得到的设备列表是:{phone_num}")
        return phone_num


def run(device_list):
    play_voice("start")
    print("开始执行抢菜程序.....")
    while True:
        try:
            qiang_cai(device_list)
        except Exception as e:
            print(e)
            play_voice("error")
            time.sleep(5)


if __name__ == '__main__':
    # 修改为设备编码
    device_list = "b8c282ac"
    run(device_list)
