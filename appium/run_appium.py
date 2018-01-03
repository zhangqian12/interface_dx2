# -*- coding:utf-8 -*-

import subprocess as sss

def get_devices():
    """获取设备号"""
    cmd = "adb devices"
    devices = sss.getoutput(cmd) #adb命令获取devices的原始信息
    if "\t" not in devices:
        print("无设备连接")
    else:
        dev_1 = devices.replace("\t"," ").replace("\n"," ") #将原始信息中的转义符号，替换为空格
        dev = dev_1.split(" ") #以空格为基准，切割字符串为列表
        print(dev[-3])
        return dev[-3] #倒数第三个元素为设备号

def runner_apm():
    """启动appium服务"""
    devices = get_devices()
    if devices == None:pass #若get_devices函数获取的设备号为空，什么也不做。
    else:
        cmd = "start appium -a 127.0.0.1 -p 4723 -U {} --session-override".format(devices) #将devices，拼接至appium启动命令中
        sss.getoutput(cmd)


runner_apm()
#get_devices()
