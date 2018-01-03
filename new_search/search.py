# -*- coding:utf-8 -*-
__author__ = 'zhangqian'


import unittest
import requests
import json
import random

class InterfaceTestCase(unittest.TestCase):

    def setUp(self):
        self.domain = 'http://search.diaox2.com'  #测试地址

        # self.domain = 'https://api.diaox2.com'   #生产地址


        self.json_headers = {'content-type':'application/json','Authorization':'diaodiao eyJhbGciOiJIUzI1NiIsImV4cCI6MTUxNDM2NjIyMywiaWF0IjoxNTE0MzYyNjIzfQ.eyJ1c2VybmFtZSI6InJkIn0.e1Io6QDbSKOOKBhTK3CbeuZ7tsJS2SrJa2JJ8gOt0Yg'}
        # self.json_headers=  {'content-type':'application/json','Authorization':self.test_login()["Authorization"]}
        self.username = "rd"
        self.password = "rd"
        self.device = {"version":"3.9.15","did":"F7A1DB2A-5F5E-48D2-8655-658B22474530","screen":"375,812","client":"ios","idfa":"213A0FFB-7679-40E1-A0E1-A793A86E1345","device":"iPhone10,3","net":"WIFI","os":"iOS 11.2.1"}


    def tearDown(self):
        print("test end")

    # /v4_search/login GET,POST 登陆
    def test_login(self):
        paras = {"username":self.username,"passwd":self.password}
        path = '/v4_search/login'
        self.post_json_paras(paras,path)

    # /v4_search/hot_queries 热门搜索query列表，GET,POST
    def test_hot_queries(self):
        paras = {}
        path = '/v4_search/hot_queries'
        self.post_json_paras(paras, path)

    #/v4_search/normal POST  普通搜索
    def test_normal(self):
        paras = {"s_type":"normal","query":"手机壳","uid":"115722","device_info":self.device,"origin":"mainFeed","page_num":1,"page_size":20}
        path = '/v4_search/normal'
        self.post_json_paras(paras,path)


    #/v4_search/index GET,POST  初始化索引   使用py脚本跑
    def test_index(self):
        paras = {}
        path = '/v4_search/index'
        self.post_json_paras(paras,path)

    #/v4_search/config/index GET,POST  配置项索引初始化    使用py脚本跑
    def test_config_index(self):
        paras = {}
        path = '/v4_search/config/index'
        self.post_json_paras(paras,path)

    #/v4_search/config/insert POST  插入一个配置项
    def test_config_insert(self):
        paras = {"configs":{"sensitive_word":{"intro":"query敏感词屏蔽","config":["习近平","张倩"]}}}
        path = '/v4_search/config/insert'
        self.post_json_paras(paras,path)

    #/v4_search/config/delete POST  删除某个配置项
    def test_config_del(self):
        paras = {"configs":["k_category_coeff"]}
        path = '/v4_search/config/delete'
        self.post_json_paras(paras,path)

    #/v4_search/config/all GET,POST 查看当前所有的配置
    def test_config_all(self):
        paras = {}
        path = '/v4_search/config/all'
        self.post_json_paras(paras,path)

    #/v4_search/config/getconfig POST  查看单个配置项
    def test_getconfig(self):
        paras={"config_name":"title_coeff"}
        path = '/v4_search/config/getconfig'
        self.post_json_paras(paras,path)

    #/v4_search/updates_needed POST 通知更新文章、sku数据（大哥通知我）

    #/v4_search/special/all GET,POST 查看当前所有特型文章数据
    def test_special_all(self):
        paras = {}
        path = '/v4_search/special/all'
        self.post_json_paras(paras,path)

    #/v4_search/special/insert POST  插入一篇特型文章数据
    def test_special_insert(self):
        """插入文章类型是article的文章"""
        paras = {"special_metas":[{"associated_query":"洗面奶","head_image":"https://c.diaox2.com/cms/diaodiao/people/yangjie.png","special_id":"899999","thumb_image":"https://content.image.alimmdn.com/cms/sites/default/files/20150721/zk/sl.jpg","author":"gc","act_type":"article","interact":"https://c.diaox2.com/view/app/?m=show&id=2423","body":"哈哈哈，请你给我增加一个小接口，让我可以测试","title":"[日常]洗漱","status":1,"timestamp":"1514261497","up_time":"","down_time":""}]}
        path = '/v4_search/special/insert'
        self.post_json_paras(paras,path)

    # /v4_search/special/insert POST  插入一篇特型文章数据
    def test_special_insert(self):
        """插入文章类型是article的文章"""
        paras = {"special_metas": [{"associated_query": "牙膏挑选器", "head_image": "https://c.diaox2.com/cms/diaodiao/people/yangjie.png","special_id": "900000","thumb_image": "https://content.image.alimmdn.com/cms/sites/default/files/20150721/zk/sl.jpg","author": "gc", "act_type": "link", "interact": "https://c.diaox2.com/view/app/?m=show&id=2423","body": "哈哈哈，请你给我增加一个小接口，让我可以测试", "title": "[日常]洗漱", "status": 1, "timestamp": "1514261497","up_time": "", "down_time": ""}]}
        path = '/v4_search/special/insert'
        self.post_json_paras(paras, path)


    #/v4_search/special/delete POST 删除一篇特型文章数据
    def test_special_del(self):
        paras = {"ids":["900000"]}
        path = '/v4_search/special/delete'
        self.post_json_paras(paras,path)

    # /v4_search/gift_showtext GET,POST 礼物筛选器筛选条件
    def test_gift_showtext(self):
        paras = {}
        path = '/v4_search/gift_showtext'
        self.post_json_paras(paras,path)

    # /v4_search/gift_search POST  礼物搜索
    def test_gift_search(self):
        paras = {"query":"鼠标","filter":{"category":"科技数码","scene":"过年回家","relation":"父母","price":[200,5000]},"uid":"115722","device_info":self.device,"origin":"mainFeed","order_type":"normal","page_num":1,"page_size":20}
        path = '/v4_search/gift_search'
        self.post_json_paras(paras,path)

    # /v4_search/gift_search_wechat POST 小程序礼物搜索
    def test_gift_search_wechat(self):
        paras = {"category":"科技数码","scene":"生日","relation":"爸爸","price":[500,1000]}
        path = '/v4_search/gift_search_wechat'
        self.post_json_paras(paras,path)

    # /v4_search/clicked_log POST 日志（三种，搜索日志、点击日志、礼物筛选条件点击日志）
    def test_clicked_log(self):
        paras = {"origin":"mainFeed","search_type":"normal","device_info":self.device,"uid":"115722","timestamp":1510308704,"query":"手机壳","log_type":"clicked","clicked":{"id":900000,"type":"article"},"clicked_order":1}
        path = '/v4_search/clicked_log'
        self.post_json_paras(paras,path)

    # /v4_search/clicked_log POST 日志（三种，搜索日志、点击日志、礼物筛选条件点击日志）
    def test_clicked_log(self):
        paras = {"origin": "mainFeed", "search_type": "gift", "device_info": self.device, "uid": "115722",
                    "timestamp": 1510308704, "query": "手机壳", "filter_clicked": "过年回家",}
        path = '/v4_search/clicked_log'
        self.post_json_paras(paras, path)

    # /v4_search/debug/normal POST 查看普通搜索得分情况
    def test_debug_normal(self):
        paras = {"s_type":"normal","query":"口红","uid":"115722","device_info":self.device,"origin":"mainFeed","page_num":1,"page_size":"20","id":900000}
        path = '/v4_search/debug/normal'
        self.post_json_paras(paras,path)

    # /v4_search/debug/gift POST 查看礼物搜索得分情况
    def test_debug_gift(self):
        paras = {"origin":"mainFeed","uid":115722,"query":"键盘鼠标","order_type":"normal","filter":{"category":"","price":[100,500],"relation":"父母","scene":""},"device_info":self.device,"page_num":2,"page_size":40}
        path = '/v4_search/debug/gift'
        self.post_json_paras(paras,path)

    # /v4_search/debug/article?id=123 GET 查看文章索引数据
    def test_debug_article(self):
        paras = {"id":900000}
        path = '/v4_search/debug/sku?id=123'
        self.get_test_interface(path)

    # /v4_search/debug/sku?id=123 GET 查看sku索引数据
    def test_debug_sku(self):
        path = '/v4_search/debug/sku?id=123'
        self.get_test_interface(path)

    # /v4_search/debug/es_status GET 搜索引擎状态、信息、配置
    def test_debug_es_status(self):
        path = '/v4_search/debug/es_status'
        self.get_test_interface(path)




########################################################################################以下为公共

    def post_json_paras(self,paras,path):
        '''传参数，拿数据请求'''
        json_data = json.dumps(paras)
        r = requests.post(self.url(path), data=json_data, headers=self.json_headers).json()
        print self.get_json(r)

        ass = self.assertEqual(r['state'],"SUCCESS")
        return self.get_json(r),ass

    def post_no_json_paras(self,paras,path):
        '''传不带json的数据'''
        r = requests.post(self.url(path), json=paras).json()
        print self.get_json(r)

        ass = self.assertEqual(r['state'],"SUCCESS")
        return self.get_json(r),ass

    # get接口
    def get_test_interface(self,path):
        print("test get ")
        result = requests.get(self.url(path)).json()
        print self.get_json(result)
        return result

    # url地址
    def url(self,path):
        '''拼接url地址'''
        return self.domain + path

    # 转json格式
    def get_json(self,json_type):
        '''转json格式'''
        json_data = json.dumps(json_type)
        return json_data


if __name__ == '__main__':
    unittest.main()