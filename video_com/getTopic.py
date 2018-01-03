# -*- coding:utf-8 -*-
__author__ = 'zhangqian'


import unittest
import requests
import json
import random

class InterfaceTestCase(unittest.TestCase):

    def setUp(self):
        self.domain = 'https://apitest.diaox2.com'  #测试地址

        # self.domain = 'https://api.diaox2.com'   #生产地址


        self.json_headers = {'content-type':'application/json'}
        self.author = [42,43,45,46,47,48,51,54,55,56,57,58,59,60,61,62,63,64,65,69]  #作者列表
        self.question_ids = [105,106,107,108,109,110,111,112,122]
        self.star_answers_parent_ids = [113,114,115,229,230,231,221,222]   #评分类型的answer对应的parent_ids
        self.mod_answers_parent_ids = [109,116,117,118,232,233,234,224]  #
        self.topic_4_skus = [316,480,3690,3695,4159,7535,9278,10007]  #topic4下拥有的sku

        self.username = "pm"
        self.password = "yjdrq123456"


    def tearDown(self):
        print("test end")

    #添加topic
    def test_add_topic(self):
        '''添加topic'''
        paras = {"title":"你会在十一期间买手机不？","cover":"http://content.image.alimmdn.com/sku/1503568326686194_jpg.jpeg","desc":"请描述一下在国庆期间，大家想要去游玩的地方，是不是都是人山人海的，还是说你会买手机？","author":115722,"pattern":{"v1":{"model":{"must":{"753":{"order":1},"754":{"order":2},"755":{"order":3},"756":{"order":4}},"option":{"757":{"order":1},"758":{"order":2},"759":{"order":3}},"option_min":1}}},"skus":[9105,6783,7730,7997,7001,601,8405,9178,7534,7384]}
        path = '/TP/addtopic'
        self.get_no_json_paras(paras,path)

    def test_mod_topic(self):
        '''修改topic'''
        paras = {"id":7,"title":"你会在十一期间买手机不？","cover":"http://content.image.alimmdn.com/sku/1503568326686194_jpg.jpeg","desc":"请描述一下在国庆期间，大家想要去游玩的地方，是不是都是人山人海的，还是说你会买手机？","author":115722,"pattern":{"v1":{"model":{"must":{"753":{"order":1},"754":{"order":2},"755":{"order":3},"756":{"order":4}},"option":{"757":{"order":1},"758":{"order":2},"759":{"order":3}},"option_min":1}}},"skus":[9105,6783,7730,7997,7001,601,8405,9178,7534,7384]}
        path = '/TP/modtopic'
        self.get_json_paras(paras,path)

    def test_mask_topic(self):
        '''屏蔽话题'''
        paras = {"id":2,"status":0,"username":self.username,"password":self.password}
        path = '/TP/masktopic'
        self.get_json_paras(paras,path)

    # get_topic拉取一个话题的详细数据
    def test_get_topic(self):
        paras = {'id':1}
        path = '/TP/gettopic'
        self.get_json_paras(paras,path)

    def test_query_topic(self):
        '''运营接口：列出话题的详情数据'''
        paras = {"id":[1,2,3,4],"status":[0,1],"title":"牙刷","author":[115722,30358],"createbefore":1505827864,"username":self.username,"password":self.password}
        path = '/TP/querytopic'
        self.get_json_paras(paras,path)

    def test_query_topic_dif_title(self):
        '''运营接口：列出status中有0的话题的详情数据'''
        paras = {"id": [1, 2, 3, 4], "status": [0, 1], "title": "iPhone", "author": 115722, "createbefore": 1505962979,"username": self.username, "password": self.password}
        path = '/TP/querytopic'
        self.get_json_paras(paras, path)


#############################################################################################################添加问题的接口

    # 添加问题
    def test_add_type0_question(self):
        '''添加模版问题,type=0,打分类型的问题'''
        titles = ["小米box","华为荣耀","魅族"]
        paras = {"title":random.choice(titles),"author":115722,"type":0,"sid":0,"tid":0}
        path = '/QE/addquestion'
        self.get_no_json_paras(paras,path)

    # 添加问题
    def test_add_type1_question(self):
        '''添加模版问题,type=1,回答类型的问题'''
        titles = ["你想买哪个牌子的手机？", "你买过xbox不？", "你喜欢魅族不？","你喜欢华为不？"]
        paras = {"title": random.choice(titles), "author": 115722, "type": 1, "sid": 0, "tid": 0}
        path = '/QE/addquestion'
        self.get_no_json_paras(paras, path)

    def test_add_type21_question(self):
        '''添加用户的回答,type=21,回答类型的问题'''
        titles = ["你用的好不好用？","颜色好不好看？","你用的是港版还是什么版？","电池的耐用程度怎么样？","通过什么渠道来订货？","我放点特殊符号,./;':<>?[]\{}|=-+_)(*&^%$#@!~`)","中文特殊符号，。、‘；：“”【】、｛｝｜+——）（*&……%￥#@！~=-"]
        paras = {"title":random.choice(titles),"author":random.choice(self.author),"type":21,"sid":random.choice(self.topic_4_skus),"tid":4}
        path = '/QE/addquestion'
        self.get_json_paras(paras,path)

    def test_question_list(self):
        '''拉取问题列表'''
        paras = {"tid":1,"sid":10007,"pagenumber":1,"pagesize":10}
        path = '/QE/questionlist'
        self.get_json_paras(paras,path)

    def test_mod_question(self):
        '''修改问题,修改问题时,不可以修改type的类型'''
        paras = {"id":753,"title":"华为荣耀手机", "author": 115722, "type": 0, "sid": 0, "tid": 0,"username":self.username,"password":self.password}
        path = '/QE/modquestion'
        self.get_json_paras(paras,path)

##########################################################################################################################

    def test_add_answer(self):
        '''添加答案,根据作者id和questionid来决定添加,如果已有则编辑'''
        paras = {"author":random.choice(self.author),"parentid":403,"content":[{"type": "text", "value": u"是支持emoji????????图片"}]}
        path = '/AN/addanswer'
        self.get_json_paras(paras,path)

    def test_mod_answer(self):
        '''修改答案'''
        paras = {"id":346,"author":random.choice(self.author),"parentid":403,"content":[{"type": "text", "value": u",./<>?;':{}[]|\+_)(*&^%$#@!~=-支持emoji????????图片"},{"height":640,"size":28429,"type":"pic","url":"https://oss.diaox2.com/ugc_pics/20170914/115722_1505372883.jpg","width":640}]}
        path = '/AN/modanswer'
        self.get_json_paras(paras,path)

    def test_del_answer(self):
        '''删除答案,check答案是否为当前用户的，是的话修改答案的status为0，否则返回'''
        paras = {"uid":random.choice(self.author),"id":346,"username":self.username,"password":self.password}
        path = '/AN/delanswer'
        self.get_json_paras(paras,path)

    def test_mask_answer(self):
        '''屏蔽答案'''
        paras = {"id":345,"status":1,"username":self.username,"password":self.password}
        path = '/AN/maskanswer'
        self.get_json_paras(paras,path)


    ##################################################################以下为体验的接口
    def test_add_exprience(self):
        '''添加体验,topic=4 的sku'''
        paras = {"author": random.choice(self.author), "tid": 4, "sid":random.choice(self.topic_4_skus), "answers": [{"question_id": 221, "question_type": 10, "content": 4},{"question_id":222,"question_type":10,"content":5},{"question_id": 224, "question_type": 11,"content": [{"type": "text", "value": "支持图片"}]}]}
        path = '/EX/addexperience'
        self.get_no_json_paras(paras,path)

    def test_mod_exprience(self):
        '''修改体验'''
        paras = {"id":25,"author": random.choice(self.author), "tid": 4, "sid": random.choice(self.topic_4_skus), "answers": [{"id":20,"question_id": 221, "question_type": 10, "content": 4},{"id":21,"question_id":222,"question_type":10,"content":5},{"id":22,"question_id": 224, "question_type": 11,"content": [{"type": "text", "value": "支持图片"}]}]}
        path = '/EX/modexperience'
        self.get_no_json_paras(paras,path)

    def test_mask_exprience(self):
        '''屏蔽体验'''
        paras = {"id":25,"status":0,"username":self.username,"password":self.password}
        path = '/EX/maskexperience'
        self.get_json_paras(paras,path)

    def test_get_exprience(self):
        '''获取体验'''
        paras = {"id":41}
        path = '/EX/getexperience'
        self.get_json_paras(paras,path)

    def test_user_experience(self):
        '''拉取话题下用户的体验'''
        paras = {"author": 30358, "tid": 1, "sid": 10007}
        path = '/EX/userexperience'
        result = self.get_json_paras(paras,path)

    def test_query_experience(self):
        '''运营接口：列出体验的详情数据'''
        pass


######################################################### 以下为SKU接口

    def test_add_owner(self):
        '''添加SKU拥有着'''
        paras = {"uid":random.choice(self.author),"sid":random.choice(self.topic_4_skus)}
        path = '/SK/addowner'
        self.get_json_paras(paras,path)

    def test_del_owner(self):
        '''删除SKU拥有者'''
        paras = {"uid":64,"sid":4681}
        path = '/SK/delowner'
        self.get_json_paras(paras,path)

    def test_check_owner(self):
        '''获取用户是否拥有指定的sku'''
        paras = {"uid":115722,"sid":1007}
        path = '/SK/checkowner'
        self.get_json_paras(paras,path)

    def test_get_sku(self):
        '''获取SKU页的详情数据'''
        paras = {"sid":2111,"tid":4,"uid":115722}
        # paras = {"sid":3285,"tid":1}
        path = '/SK/getsku'
        self.get_json_paras(paras,path)

    def test_query_sku(self):
        '''列出SKU的详情数据,id为skuid'''
        paras = {"id":[9458,10007,10262],"tid":[1,2],"qid":[238,252,258],"username":self.username,"password":self.password}
        path = '/SK/querysku'
        self.get_json_paras(paras,path)

########################################################################################以下是评论相关

    def test_add_comment(self):
        '''添加评论'''
        paras = {"author":30358,"parenttype":'CO',"parentid":1,"content":[{"type":"text","value":"我是评论"}]}
        path = '/CO/addcomment'
        self.get_json_paras(paras,path)

    def test_mod_comment(self):
        '''修改评论'''
        paras = {"id":12,"author":30358,"parenttype":'CO',"parentid":1,"content":[{"type":"text","value":"我是评论,./;':[]{}\|+_=-)(*&^%$#@!~"}]}
        path = '/CO/modcomment'
        self.get_json_paras(paras,path)

    def test_mask_comment(self):
        '''屏蔽评论'''
        paras = {"id":12,"status":1,"username":self.username,"password":self.password}
        path = '/CO/maskcomment'
        self.get_json_paras(paras,path)

    def test_get_comment_list(self):
        '''获取评论'''
        paras = {"parenttype":'CO',"parentid":1,"pagenumber":1,"pagesize":10}
        path = '/CO/commentlist'
        self.get_json_paras(paras,path)

    def test_get_comment(self):
        '''获取评论详情'''
        paras = {"id":135}
        path = '/CO/getcomment'
        self.get_json_paras(paras,path)

    def test_query_comment(self):
        ''''''
        paras = {"id":[],"parenttype":[],"parentid":[],"status":[0,1],"author":random.choice(self.author)}


###########################################################################################推送消息

    def test_push(self):
        '''推送消息'''
        paras = {"push_type":"topic_question","qid":1060,"uid":[115722,191779,55,360833],"title":"有人在你拥有的XXsku下提出了问题XX","username":self.username,"password":self.password}
        path = 'http://bj3.a.dx2rd.com:9999/v1/topic/push'

        r = requests.post(path,data=json.dumps(paras),headers=self.json_headers).json()

        print self.get_json(r)


############################################################################################添加黑名单

    def test_black_name(self):
        '''添加黑名单'''
        paras = {'uid':360833,'username':self.username,'password':self.password}
        path = '/TP/userprivilege/add'

        self.get_json_paras(paras,path)


    def test_del_black_name(self):
        '''删除黑名单'''
        paras = {'uid':360833,'username':self.username,'password':self.password}
        path = '/TP/userprivilege/del'

        self.get_json_paras(paras,path)

    def test_black_name_list(self):
        '''查看黑名单列表'''
        paras = {'uid':[115722,50726],'topic':[255,0],'pagenumber':1,'pagesize':1000,'username':self.username,'password':self.password}
        path = '/TP/userprivilege/query'

        self.get_json_paras(paras,path)

############################################################################################文章内链加积分
    #连接美西服务器
    def test_add_comment_jifen(self):
        '''{"action": "xxx", "uid": 123, "person": "LYN", "code": "xxxx", "reason": "理由"}
        action: "comment"，针对文章评论活动进行的加减分，线下调用
        其他参数："uid": 这里uid是虚拟参数，需要提供，但是实际无用
        其他参数："cid": 文章的id，根据文章，去找评论
        其他参数："stamp": 截止时间，早于这个时间戳的评论，才加积分
        其他参数："value": 加的几分数，注意只能是正数
        '''
        paras = {"action": "comment", "uid": 50726, "person": "LYN", "code": "Sohappy@1902", "reason":"某篇评论","cid":35283156344855,"stamp":1479823070,"value":50}
        path = 'http://usw1.a.dx2rd.com:3000/jf/set_state'

        r = requests.post(path,data=json.dumps(paras),headers=self.json_headers).json()

        print self.get_json(r)

########################################################################################### 新修改的topic的接口
    def test_alltopic(self):
        """拉取一个话题的详细数据"""
        paras = {"pagesize":10,"pagenumber":1}
        path = "/TP/alltopic"
        self.get_json_paras(paras,path)

    def test_up(self):
        """测试评测的点赞"""
        paras = {"uid":115723,"like":1,"parenttype":"EX","parentid":446}
        path = '/TP/up'
        self.get_json_paras(paras,path)

    def test_up(self):
        """测试答案的点赞"""
        paras = {"uid":115722,"like":1,"parenttype":"AN","parentid":1210}
        path = '/TP/up'
        self.get_json_paras(paras,path)

    def test_unup(self):
        """取消点赞"""
        paras = {"uid": 115722, "like": 0, "parenttype": "AN", "parentid": 1210}
        path = '/TP/up'
        self.get_json_paras(paras, path)

    def test_gettopic(self):
        """获取话题页"""
        paras = {"id":10}
        path = '/v2/TP/gettopic'
        self.get_json_paras(paras,path)

    def test_topic_featured(self):
        """"话题中没有评测时，拉取精选"""
        paras = {"tid":10,"pagesize":11,"pagenumber":1}
        path = '/TP/featured'
        self.get_json_paras(paras,path)

    def test_topic_featured(self):
        """话题中有评测时，拉取精选"""
        paras = {"tid":1,"pagesize":11,"pagenumber":1}
        path = '/TP/featured'
        self.get_json_paras(paras,path)

    def test_new_experience(self):
        """测试新评测"""
        paras = {"tid":10,"pagesize":10,"pagenumber":1}
        path = '/TP/experience'
        self.get_json_paras(paras,path)

    def test_new_answer(self):
        """测试新问答页"""
        paras = {"tid":10,"pagesize":10,"pagenumber":1}
        path = '/TP/answer'
        self.get_json_paras(paras,path)

    def test_new_all_sku(self):
        """测试全部商品页"""
        paras = {"tid":1,"sort":'score'}
        path = '/TP/allsku'
        self.get_json_paras(paras,path)

    def test_new_getsku(self):
        """测试获取新商品页"""
        paras = {"sid":1,"tid":1,"pagenumber":1,"pagesize":10}
        path = '/v2/SK/getsku'
        self.get_json_paras(paras,path)

    def test_new_questionlist(self):
        """测试新全部问题页"""
        paras = {"tid":10,"sid":20001,"pagenumber":1,"pagesize":11}
        path = '/v2/QE/questionlist'
        self.get_json_paras(paras,path)

    def test_new_get_experience(self):
        """新评测详情"""
        paras = {"id": 41}
        path = '/v3/EX/getexperience'
        self.get_json_paras(paras, path)

    def test_new_get_question(self):
        """新问题详情"""
        paras = {"id":1,"pagenumber":1,"pagesize":10}
        path = '/v2/QE/getquestion'
        self.get_json_paras(paras,path)

    def test_new_get_new_answer(self):
        """新答案详情页"""
        paras = {"id":1,"uid":115722}
        path = '/v2/AN/getanswer'
        self.get_json_paras(paras,path)

    def test_new_query_experience(self):
        """拉取评测"""
        paras = {}
        path = '/EX/queryexperience'
        self.get_json_paras(paras,path)

    def test_new_query_answer(self):
        """拉取答案"""
        paras = {}
        path = '/AN/queryanswer'
        self.get_json_paras(paras,path)

    def test_add_type2_question(self):
        """添加type=2的综合评分的问题"""
        paras = {"title":"综合评分", "author": 115722, "type": 2, "sid": 0, "tid": 0}
        path = '/QE/addquestion'
        self.get_json_paras(paras,path)

    def test_new_add_topic(self):
        """新添加topic"""
        paras = {"title":"新修改的话题多一个综合打分项","cover":"http://content.image.alimmdn.com/sku/1503568326686194_jpg.jpeg","desc":"请描述一下在国庆期间，大家想要去游玩的地方，是不是都是人山人海的，还是说你会买手机？","author":115722,"pattern":{"v1":{"model":{"must":{"1513":{"order":1},"1506":{"order":2},"1507":{"order":3},"1508":{"order":4},"1509":{"order":5}},"option":{"1510":{"order":1},"1511":{"order":2}},"option_min":0}}},"skus":[9105,6783,7730,7997,7001,601,8405,9178,7534,7384]}
        path = '/TP/addtopic'
        self.get_json_paras(paras,path)

    def test_new_mod_topic(self):
        """新修改topic"""
        paras = {"id":7,"title":"你会在十一期间买手机不？","cover":"http://content.image.alimmdn.com/sku/1503568326686194_jpg.jpeg","desc":"请描述一下在国庆期间，大家想要去游玩的地方，是不是都是人山人海的，还是说你会买手机？","author":115722,"pattern":{"v1":{"model":{"must":{"1495":{"order":1},"753":{"order":2},"754":{"order":3},"755":{"order":4},"756":{"order":5}},"option":{"757":{"order":1},"758":{"order":2},"759":{"order":3}},"option_min":1}}},"skus":[9105,6783,7730,7997,7001,601,8405,9178,7534,7384]}
        path = '/TP/modtopic'
        self.get_json_paras(paras,path)

    def test_new_mod_question(self):
        """新修改question"""
        paras = {"id":753,"title":"华为荣耀手机", "author": 115722, "type": 0, "sid": 0, "tid": 0,"username":self.username,"password":self.password}
        path = '/QE/modquestion'
        self.get_json_paras(paras,path)



########################################################################################以下为公共

    def get_json_paras(self,paras,path):
        '''传参数，拿数据请求'''
        json_data = json.dumps(paras)
        r = requests.post(self.url(path), data=json_data, headers=self.json_headers).json()
        print self.get_json(r)

        ass = self.assertEqual(r['state'],"SUCCESS")
        return self.get_json(r),ass

    def get_no_json_paras(self,paras,path):
        '''传不带json的数据'''
        r = requests.post(self.url(path), json=paras).json()
        print self.get_json(r)

        ass = self.assertEqual(r['state'],"SUCCESS")
        return self.get_json(r),ass

    # def check_result(self,result):
    #     '''校验结果'''
    #     return self.assertEqual(result,"SUCCESS")
    #     # return  self.assertEqual(result['state'],"SUCCESS")

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