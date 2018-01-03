# -*- coding:utf-8 -*-
__author__ = 'zhangqian'

import unittest
import json
import requests
import time
from requests.auth import HTTPBasicAuth


class Get_goods_list(unittest.TestCase):

    def setUp(self):
        self.base_url = 'https://api-ec.diaox2.com'
        print("start test")

    def tearDown(self):
        print("end test")


    def test_goods_list(self):

        # 验证获取
        self.url= self.base_url + '/v1/ec_index'
        param = {'uid':1,'page':2,'number':40,'last_goods_time':''}
        response = requests.get(self.url,params=param).json()
        print(response)
        # self.assertEqual(response.get('data').get('nick_name'),"Ruby133")
        # self.assertEqual(response.get('data').get('nick_name'),"Ruby133")
        self.assertEqual(response.get('errmsg'),"ok")




if __name__ == "__main__":
    # unittest.main()  #执行全用例

    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Get_goods_list('test_goods_list')) #测试单个用例，将用例名加入

    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
