# -*- coding:utf-8 -*-
'''本段代码非淘宝，而是本人实际操作的app'''
import os, time, unittest
from selenium import webdriver


PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

desired_caps = {}
desired_caps['platformName'] = 'Android'  # 设备系统
desired_caps['platformVersion'] = '4.4.4'  # 设备系统版本
desired_caps['deviceName'] = 'MI3'  #  设备名称

desired_caps['app'] = PATH(r"D:\apk\YouDiaoceshi3910.apk")
desired_caps['appPackage'] = 'com.diaox2.android'
desired_caps['appActivity'] = 'com.diaox2.android.activity.SplashActivity'


driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
time.sleep(5)