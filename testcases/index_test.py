#  -*-  coding:utf-8 -*-
import requests
import json


class TestIndex():
    def test_index_info(self):
        host = 'http://192.168.0.174:8888'
        path = '/api/v1/index-infos'
        res = requests.request('GET', url=host + path, headers=None, params=None)
        res_json = res.json()
        print("接口返回结果：" + json.dumps(res_json))
        assert res_json['resultCode'] == 200
        assert res_json['data']['carousels'] is not None
