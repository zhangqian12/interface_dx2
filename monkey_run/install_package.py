# -*- coding:utf-8 -*-
__author__ = 'zhangqian'

#导入包
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice

device=MonkeyRunner.waitForConnection()
device.installPackage('D:\\apk\\YouDiaoceshi3910.apk')
MonkeyRunner.sleep(3.0)

#com.diaox2.android.activity.SplashActivity
runComponent = "com.diaox2.android/.activity.SplashActivity"

device.startActivity(component=runComponent)