#coding=utf-8
from selenium import webdriver
from appium import webdriver
import os
import unittest

class InterfaceTestCase(unittest.TestCase):

    def device_info(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        # desired_caps['deviceName'] = '84B5T15A10009935'  # 华为NEXUS6
        desired_caps['deviceName'] = 'abff62f1'  # 小米5
        desired_caps['appPackage'] = 'com.diaox2.android'
        desired_caps['appActivity'] = 'com.diaox2.android.activity.SplashActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)

    def quit(self):
        self.driver.quit()

    def install_app(self):
        self.driver.install_app()

# driver.find_element_by_name("1").click()
#
# driver.find_element_by_name("5").click()
#
# driver.find_element_by_name("9").click()
#
# driver.find_element_by_name("delete").click()
#
# driver.find_element_by_name("9").click()
#
# driver.find_element_by_name("5").click()
#
# driver.find_element_by_name("+").click()
#
# driver.find_element_by_name("6").click()
#
# driver.find_element_by_name("=").click()

driver.quit()
