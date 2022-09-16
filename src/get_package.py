import uiautomator2 as u2

# 第2种连接手机的USB进行连接(安卓模拟器和真机都可以）必须开启USB调试模式
# RFCN309ABWX为手机序列号，`adb devices`查看
# d = u2.connect("RFCN309ABWX")
d = u2.connect("192.168.31.194:5566")
# 查看当前app的包名称
info = d.info
print(info)