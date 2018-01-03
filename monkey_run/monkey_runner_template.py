# -*- coding:utf-8 -*-
__author__ = 'zhangqian'

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

device.startActivity(component=componentName)

#monkeyrunner按键

#发送指定键的关键事件：　　
"""device.press(参数1：键码, 参数2:触摸事件类型)"""

"""参数1：常用键内容"""

#按下HOME键
device.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)

#按下BACK键
device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)

#按下下导航键
device.press('KEYCODE_DPAD_DOWN', MonkeyDevice.DOWN_AND_UP)

#按下上导航键
device.press('KEYCODE_DPAD_UP', MonkeyDevice.DOWN_AND_UP)

#按下OK键
device.press('KEYCODE_DPAD_CENTER', MonkeyDevice.DOWN_AND_UP)

#按下左导航键
device.press('KEYCODE_DPAD_LEFT', MonkeyDevice.DOWN_AND_UP)

#按下右导航键
device.press('KEYCODE_DPAD_RIGHT', MonkeyDevice.DOWN_AND_UP)

"""相应的按键对应名称："""

#menu键：
KEYCODE_MENU

#home键：
KEYCODE_HOME

#back键：
KEYCODE_BACK

#search键：
KEYCODE_SEARCH

#call键：
KEYCODE_CALL

#end键：
KEYCODE_ENDCALL

#上音量键：
KEYCODE_VOLUME_UP

#下音量键：
KEYCODE_VOLUME_DOWN

#power键：
KEYCODE_POWER

#camera键：
KEYCODE_CAMERA

#monkeyrunner卸载包

device.removePackage ('com.example.android.notepad')

print ('卸载成功')

#monkeyrunner安装包

device.installPackage('ApiDemos.apk')
print ('安装成功')

#monkeyrunner单击控件

#方式1：
device.touch(507,72,"DOWN_AND_UP")


#方式2：
easy_device.touch(By.id('id/qingchu'),device.DOWN_AND_UP)

"""用方式2需要导入

from com.android.chimpchat.hierarchyviewer import HierarchyViewer #根据ID找到ViewNode，对viewnode的一些操作等

from com.android.monkeyrunner.easy import EasyMonkeyDevice  #提供了根据ID进行访问方法touch、drag等

from com.android.monkeyrunner.easy import By    #根据ID返回PyObject的方法

from com.android.hierarchyviewerlib.models import ViewNode as vn #代表一个控件，可获取控件属性
"""

#monkeyrunner长按控件

#方式1：
device.touch(507,72,"DOWN_AND_UP")

device.touch(507,72,MonkeyDevice.DOWN)

MonkeyRunner.sleep(1)
device.touch(507,72,MonkeyDevice.UP)

#方式2：
easy_device.touch（By.id('id/qingchu'),,MonkeyDevice.DOWN)
MonkeyRunner.sleep(1)
easy_device.touch(By.id('id/qingchu'),MonkeyDevice.UP)

"""用方式2需要导入
from com.android.chimpchat.hierarchyviewer import HierarchyViewer #根据ID找到ViewNode，对viewnode的一些操作等
from com.android.monkeyrunner.easy import EasyMonkeyDevice  #提供了根据ID进行访问方法touch、drag等
from com.android.monkeyrunner.easy import By    #根据ID返回PyObject的方法
from com.android.hierarchyviewerlib.models import ViewNode as vn #代表一个控件，可获取控件属性"""

#monkeyrunner滑动屏幕

for i in range(1,70):

    device.drag((250,110),(250,850),0.1,10)

    MonkeyRunner.sleep(1)

    #monkeyrunner延时

    MonkeyRunner.sleep(3)

    #monkeyrunner截图

    result = device.takeSnapshot()

    result.writeToFile('C:\\Users\\Martin\\Desktop\\test.png','png')

    #monkeyrunner截图对比

    result1.sameAs(result0,1.0)


    #monkeyrunner局部图片（前两个值是左上角左边，后两个值是右下角减左上角的坐标。）

    pic0= result0.getSubImage((4,41,400,700))

    #monkeyrunner重启设备

    device.reboot()

    #monkeyrunner单击电源键，熄灭屏幕

    device.press('KEYCODE_POWER',MonkeyDevice.DOWN_AND_UP)

    #monkeyrunner唤醒屏幕

    device.wake()

    #monkeyrunner输入文本

    Cotent='1234'

    device.type(Cotent)
