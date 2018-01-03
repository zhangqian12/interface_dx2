# -*- coding:utf-8 -*-
__author__ = 'zhangqian'

import sys
print (sys.path)

#monkeyrunner导入模块
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

#monkeyrunner连接设备
device = MonkeyRunner.waitForConnection()
if not device:
    print "Please connect a device to start!"
else:
    print "Start "

#monkeyrunner启动一个Activity
componentName="com.ss.android.article.news/.activity.SplashActivity"