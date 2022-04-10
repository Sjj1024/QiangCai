# QiangCai
上海疫情被封在家，开始抢菜之路，可以开启多台设备同时抢菜

个人微信/QQ：2950525265，有问题可以咨询



使用说明：
博客教程地址：https://xiaoshen.blog.csdn.net/article/details/124069742（被封了，不知道原因）

上海现在抢菜之苦，真的有口说不出，每天早上6点，6点半，8点半，体验过的人的都知道，即便手速再快，还是抢不到.....
然后就有了下面的抢菜程序，完全由Python实现，并会附上教程：

一.安装环境
python3：安装python3环境，并安装依赖：
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --pre -U uiautomator2
adb：您可以转到[官方文档]（https://developer.android.com/studio/command-line/adb）
( mac电脑adb安装：brew install android-platform-tools )
手机：安卓手机一部或者多部，或者安卓虚拟机一个或者多个

二.调试环境
adb：adb安装成功后，在命令行输入adb，会出现以下提示：
![](https://img-blog.csdnimg.cn/140a1fc0bd3d44a1a226ee3fee6b9a89.png)
adb start-server：启动服务
adb devices：查看连接的设备列表
当安卓手机和电脑连接之后，再输入：adb devices，就可以看到设备编号，记住这个编号，后面有用。
（如果用的安卓虚拟机，需要注意：需要先执行：adb kill-server，然后再执行：adb start-server，再执行：adb devices，才会显示设备列表）
![](https://img-blog.csdnimg.cn/ae2e00c88c6a473f80946d07d5677ce0.png)
设备上安装atx-agent：
python -m uiautomator2 init 
会在安卓设备上安装一个依赖ATX软件：
![](https://img-blog.csdnimg.cn/4349aac9a9334b629141628e94bf8c84.png)

三.开始抢菜
打开美团，并进入购物车页面，确认购物车里是有商品的：（没有商品肯定是不行的，对吧）
![](https://img-blog.csdnimg.cn/abc35dbaedc044b9b11e42f0d5f35313.png)
然后开始运行代码： 
python meituan.py

最后看一下成果：
（因为我有两个安卓手机，又另外开了一个安卓虚拟机，所以就是下面效果了，哈哈哈哈哈）
![](https://img-blog.csdnimg.cn/a561fae90f80420c9be3ae9ee9560da7.gif)

再展示一下抢到的菜吧，同时祝大家早日抢到自己喜欢的菜吧，也希望疫情赶紧结束：
![](https://img-blog.csdnimg.cn/86b6a70bdd14416e868ac566cea08657.png)