# -*- coding:utf-8 -*-
__author__ = 'zhangqian'


import unittest
import requests
import json

class InterfaceTestCase(unittest.TestCase):

    def setUp(self):
        self.domain = 'https://api-ec.diaox2.com'
        self.json_headers = {'content-type':'application/json'}

    def tearDown(self):
        print("after")

    # 获取全部商品
    def test_get_all_goods(self):
        print("test get all goods")
        result = requests.get(self.url("/v1/ec_index")).json()
        print ('the new goods number is %d:'% (len(result['new_goods'])))
        print ('all goods number is %d:' % (len(result['all_goods'])))
        print ('last_goods_time is %s:' % (result['time']))

        self.assertEqual(result['errmsg'],'ok')
        if result['page'] == 1:
            self.assertEqual(result['number'],6)

    #获取商品的分类页
    def test_get_all_tags(self):
        print ("test get all tags")
        result = requests.get(self.url("/v1/ec_tab")).json()

        print result

        self.assertEqual(result['errmsg'],'ok')
        if result['page'] == 1:
            self.assertEqual(result['number'],6)

    #获取商品详情,测试price_type=1仅金额购买
    def test_get_good_detail_1(self):
        print ("test get good detail price_type=1")
        param = {'gid':206}
        share_title = u'高颜值铸铁锅，煎炒烹炸炖煮全包办'

        # result = requests.get(self.url("/v1/goods_detail?gid=206"))
        result = requests.get(self.url("/v1/goods_detail"),params=param).json()
        print result

        if result['price_type'] == 1:
            self.assertEqual(result['score'],0)
            self.assertEqual(result['g_price'],'0.00')
            self.assertEqual(result['g_score'],0)
            self.assertNotEqual(result['price'],0)
        print result['share_title']
        self.assertEqual(result['share_title'],share_title)
        self.assertEqual(result['errmsg'],'ok')

    # 获取商品详情,测试price_type=2仅积分购买
    def test_get_good_detail_2(self):
        print ("test get good detail price_type=2")
        param = {'gid':205}
        share_title = u'牙刷'

        result = requests.get(self.url("/v1/goods_detail"),params=param).json()

        print result

        if result['price_type'] == 2:
            self.assertEqual(result['price'],'0.00')
            self.assertEqual(result['g_price'],'0.00')
            self.assertEqual(result['g_score'],0)
            self.assertNotEqual(result['score'],0)

        print(result['share_title'])
        self.assertEqual(result['share_title'],share_title)
        self.assertEqual(result['errmsg'],'ok')

    # 获取商品详情,测试price_type=3仅价格或仅积分购买
    def test_get_good_detail_3(self):
        print ("test get good detail price_type=3")
        param = {'gid':135}
        share_title = u'我们把最好写的笔，都为你打包好了'

        result = requests.get(self.url("/v1/goods_detail"),params=param).json()

        print result

        if result['price_type'] == 3:
            self.assertNotEqual(result['price'],'0.00')
            self.assertNotEqual(result['score'],0)
            self.assertEqual(result['g_price'],'0.00')
            self.assertEqual(result['g_score'],0)

        print (result['share_title'])
        self.assertEqual(result['share_title'],share_title)
        self.assertEqual(result['errmsg'],'ok')

    # 获取商品详情,测试price_type=4 钱或积分+钱购买
    def test_get_good_detail_4(self):
        print ("test get good detail price_type=4")
        param = {'gid':103}
        share_title = u'五一出行，要你里面和外面一样美的不可方物！！'

        result = requests.get(self.url("/v1/goods_detail"),params=param).json()

        print result

        if result['price_type'] == 4:
            self.assertNotEqual(result['price'],'0.00')
            self.assertEqual(result['score'],0)
            self.assertNotEqual(result['g_price'],'0.00')
            self.assertNotEqual(result['g_score'],0)

        print (result['share_title'])
        self.assertEqual(result['share_title'],share_title)
        self.assertEqual(result['errmsg'],'ok')

    # 获取商品详情,测试price_type=5 积分或积分+钱购买
    def test_get_good_detail_5(self):
        print ("test get good detail price_type=5")
        param = {'gid':168}
        share_title = u''


    def url(self,path):
        return self.domain + path


if __name__ == '__main__':
    unittest.main()