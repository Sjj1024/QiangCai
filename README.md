# QiangCai
上海疫情被封在家，开始抢菜之路，可以开启多台设备同时抢菜.  
个人微信：sxsuccess，加时请说明来意，否则不通过。    
<font color='red'>有任何问题请先群聊，私聊不回复，忙不过来。如果需要私聊帮助，请先发个咖啡红包。 </font>   
微信群，因为人数超200，加微信邀请你进抢菜群，如果此工具对你有帮助，可赞赏支持：  
![](https://1024shen.com/wp-content/uploads/2022/04/2022041504273946.png)


使用说明：  
博客教程地址：https://1024shen.com/archives/7493  
远程协助软件地址：https://www.todesk.com/download.html


上海现在抢菜之苦，真的有口说不出，每天早上6点，6点半，8点半，体验过的人的都知道，即便手速再快，还是抢不到.....
然后就有了下面的抢菜程序，完全由Python实现，并会附上教程：(兼容mac和windows平台，抢成功后会播放声音提醒)


## 一.安装环境
安装python3环境:  
Mac电脑:   
如果没有brew，先安装brew:
```
/bin/zsh -c "$(curl -fsSL https://gitee.com/cunkai/HomebrewCN/raw/master/Homebrew.sh)"
```
然后再执行：
```python
brew install python
```
Windows电脑：  
windows10以上下载链接: https://wwd.lanzouf.com/i6AEm02zzppi  （安装的时候记得勾选 add python to path）
windows7以上下载链接: https://wwd.lanzouf.com/i55kC02zzqsh （安装的时候记得勾选 add python to path）

进入QiangCai文件夹，并安装依赖： 或者pip3
```python
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```
或者：
```python
pip install playsound -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --pre -U uiautomator2
```

adb：您可以转到[官方文档]（https://developer.android.com/studio/command-line/adb）  
mac电脑adb安装：
```python
brew install android-platform-tools  
```
windows adb安装:   
下载链接：https://wwd.lanzouf.com/iQWJT02zyz0h  
1.解压  
解压到任意目录,例如我都放在D:\Program Files文件夹下面   
这样adb的目录就是D:\Program Files\platform-tools  
2.添加环境变量  
此电脑->系统属性->高级系统设置->环境变量->系统变量->Path->添加->D:\Program Files\platform-tools  
（如果不想装adb，在项目的sources目录下带有win和mac的adb依赖，直接进入文件夹，运行adb也行。但不保证兼容每个设备）  
安卓手机：安卓手机一部或者多部，或者安卓虚拟机一个或者多个，安装有美团外卖或者叮咚买菜  
美团外卖下载：https://wwd.lanzouf.com/iGVRg031d9sf  
叮咚买菜下载：https://wwd.lanzouf.com/izLDB0362tja  

## 二.调试环境
现将手机和电脑链接。当安卓手机和电脑连接之后，再输入：  
adb：adb安装成功后，在命令行输入adb，会出现以下提示：
![](https://img-blog.csdnimg.cn/140a1fc0bd3d44a1a226ee3fee6b9a89.png)
adb start-server：启动服务   
adb devices：查看连接的设备列表    
adb devices，就可以看到设备编号，记住这个编号，后面有用。    
强烈推荐使用安卓虚拟机网易MUMU，官网地址：https://mumu.163.com/mac/index.html
（如果用的安卓虚拟机，需要注意：开启root权限，然后执行：adb kill-server，然后再执行：adb start-server，再执行：adb devices，才会显示设备列表）
![](https://img-blog.csdnimg.cn/ae2e00c88c6a473f80946d07d5677ce0.png)  
设备上安装atx-agent：或者python3
```python
python -m uiautomator2 init 
```
会在安卓设备上自动安装一个依赖ATX软件：  
![](https://img-blog.csdnimg.cn/4349aac9a9334b629141628e94bf8c84.png)
  
## 三.开始抢菜
打开美团买菜，并进入购物车页面，确认购物车里是有商品的：（没有商品肯定是不行的，对吧）
![](https://img-blog.csdnimg.cn/abc35dbaedc044b9b11e42f0d5f35313.png)

用记事本打开meituan.py，修改源代码中的设备编码（改为你自己的，adb devices命令执行后得到的结果中的）：
![](https://img-blog.csdnimg.cn/834563085e7046d0b4117d802da639a3.png)

1.开始美团APP代码：  
下载美团APP，进入美团买菜入口，然后进入购物车页面，运行下面代码即可  
```python
python meituan.py
或者：
python3 meituan.py
```

2.开始美团买菜APP代码：  
下载美团买菜，然后进入购物车页面，运行下面代码即可  
```python
python meituan_maicai.py
或者：
python3 meituan_maicai.py
```

3.开始叮咚APP抢菜：  
```python
python dingdong.py
或者
python3 dingdong.py
```

多设备运行：  
复制meituan.py 或者dingdong.py，修改复制文件中的设备编号，然后执行开始程序即可。  
 
最后看一下成果：
（因为我有两个安卓手机，又另外开了一个安卓虚拟机，所以就是下面效果了，速度没有图中那么快，正常1-3s点击一次）
![](https://img-blog.csdnimg.cn/a561fae90f80420c9be3ae9ee9560da7.gif)

再展示一下抢到的菜吧，同时祝大家早日抢到自己喜欢的菜吧，也希望疫情赶紧结束：
![](https://img-blog.csdnimg.cn/86b6a70bdd14416e868ac566cea08657.png)


## 常见问题汇总：  
1.使用网易的mumu模拟器过程中发现不能正常获取设备码。
通过执行adb connect 127.0.0.1:7555 (7555是模拟器端口，其他模拟器可以改一下)连接到模拟器，代码里的设备码填写127.0.0.1:7555，经测试可正常使用。  
  
2.adb devices找不到设备，或者手机安装不上那个ATX软件。  
打开手机的开发者模式，并且授权电脑所有权限，或者授权文件传输。