#-*-coding:utf-8-*-

import requests
import unittest
import json


class feed(unittest.TestCase):

    def setUp(self):
        '''均为post请求'''
        self.worth_buy_feed_url = "https://zdm.diaox2.com/dd_zdm/v1/get_feedlist"
        self.worth_buy_check_url = "https://zdm.diaox2.com/dd_zdm/check_update"
        self.worth_buy_log = "https://api.diaox2.com/general_log"

        self.feed_url = "https://api.diaox2.com/general_log"
        self.check_url = "https://zdm.diaox2.com/dd_zdm/check_update"
        self.log = "https://api.diaox2.com/expansion_log"

        self.test_url = "https://api.diaox2.com/v5/zdm"

        self.json_headers = {'content-type': 'application/json'}

    def tearDown(self):
        print("test after")

    # def test_worth_buy_check_url(self):
    #     url = self.worth_buy_check_url
    #     paras = {"client_data_version":49209728,"device_info":{"app":u"有调3.8.1 461237.397528646","client":"ios","device":"iPhone 9,2","did":"8A4BB0F8-B127-4BC5-A63F-51FCF92112B3","disk":"127989493760","idfa":"929E68E0-F5DD-435B-982B-BF7075F8683A","net":"UNKNOWN","os":"iOS 10.3.2","screen":"414.000000,736.000000","version":"3.8.1"}}
    #
    #     r = requests.post(url,data=paras)
    #     self.assertEqual(r.status_code,200)
    #     print (r)

    def test_create_feed(self):
        paras = {"client_data_version":49209728,"device_info":{"app":u"有调3.8.1 461237.397528646","client":"ios","device":"iPhone 9,2","did":"8A4BB0F8-B127-4BC5-A63F-51FCF92112B3","disk":"127989493760","idfa":"929E68E0-F5DD-435B-982B-BF7075F8683A","net":"UNKNOWN","os":"iOS 10.3.2","screen":"414.000000,736.000000","version":"3.8.1"}}
        json_data = json.dump(paras)
        r = requests.post(self.url('/posts'), data=json_data, headers=self.json_headers)
        result = r.json()

        self.assertEqual(r.status_code, 200)
        self.assertEqual(result['success'], 'ture')


    # def test_url(self):
    #     url = self.test_url
    #     paras = {"client_data_version":1497943501,"device_info":{"client":"ios","did":"99602204-0BA1-4F64-A983-F7E5C257641F","idfa":"C45A51E6-775C-4208-BC7D-21BDDCCA90EA","net":"WIFI","os":"iOS 10.3.1","version":"3.8.1"},"version_page":1}
    #
    #     r = requests.post(url,data=paras)
    #     self.assertEqual(r.status_code,200)
    #     print(r)

if __name__ == '__main__':
    unittest.main()