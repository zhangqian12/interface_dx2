# -*- coding:utf-8 -*-
__author__ = 'zhangqian'

import unittest
import json
import requests
import time
from requests.auth import HTTPBasicAuth


class Get_teacherInfo(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://test.cafeabc.cn'
        print("start test")

    def tearDown(self):
        print("end test")

    def test_teacherInfo(self):

        #验证老师的个人信息
        self.url= self.base_url + '/api/teacherInfo'
        param = {'tea_id':60}
        response = requests.get(self.url,params=param).json()
        # print(response)
        self.assertEqual(response.get('data').get('nick_name'),"Ruby133")
        self.assertEqual(response.get('errMsg'),"ok")

    def test_stuComments(self):
        u"""访问url = /api/teacherComments ， 参数param = {'tea_id':60,'page':2,'number':10} """
        #学生给老师的评价
        self.url = self.base_url + '/api/teacherComments'
        param = {'tea_id':60,'page':2,'number':10}
        response = requests.get(self.url,params=param).json()
        # print(response)
        # print(response.get('data')[0].get('message'))
        self.assertEqual(response.get('data')[0].get('message'),"commenttext")




if __name__ == "__main__":
    # unittest.main()  #执行全用例

    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Get_teacherInfo('test_teacherInfo')) #测试单个用例，将用例名加入
    suite.addTest(Get_teacherInfo('test_stuComments'))

    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
