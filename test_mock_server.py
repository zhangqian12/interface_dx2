# -*- coding:utf-8 -*-
__author__ = 'Administrator'


import unittest
import requests
import json

class InterfaceTestCase(unittest.TestCase):

    def setUp(self):
        self.domain = 'http://localhost:12306'
        self.json_headers = {'content-type':'application/json'}

    def tearDown(self):
        print("after")

    def test_get_all_post(self):
        print("test get all post")
        result = requests.get(self.url("/post")).json()

        self.assertEqual(len(result),3)

        self.assertEqual(result[0]['title'],'first post')
        self.assertEqual(result[0]['url'],'/posts/1')

        self.assertEqual(result[-1]['title'],'how to learn interface test')
        self.assertEqual(result[-1]['url'],'/posts/3')

    def test_get_first_post(self):
        print('test get first post')
        result = requests.get(self.url("/post/1")).json()

        self.assertEqual(result['title'],'first post')
        self.assertEqual(result['content'],'this is my first post')

    def test_create_post(self):
        json_data = json.dump({'title':'the new post title ','content':'the new post content'})
        r = requests.post(self.url('/posts'),data=json_data,headers=self.json_headers)
        result = r.json()

        self.assertEqual(r.status_code,200)
        self.assertEqual(result['success'],'ture')

    def test_edit_post(self):
        json_data = json.dump({'title':'the new post title ','content':'the new post content'})
        r = requests.post(self.url('/posts'),data=json_data,headers=self.json_headers)
        result = r.json()

        self.assertEqual(r.status_code,200)
        self.assertEqual(result['success'],'ture')

    def test_delete_post(self):
        r = requests.delete(self.url('/posts/2'))
        result = r.json()

        self.assertEqual(r.status_code,200)
        self.assertEqual(result['success'],'ture')

    def url(self,path):
        return self.domain + path


if __name__ == '__main__':
    unittest.main()