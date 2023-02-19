#  -*-  coding:utf-8 -*-
import requests
import json


class TestOrderList():
    def test_order_list_all(self):
        host = 'http://192.168.0.174:8888'
        path = '/api/v1/order?pageNumber=1&status='
        header = {'token':'0e6f790d865873ead9156ab7905bd177'}
        res = requests.request('GET', url=host + path, headers=header, params=None)
        res_json = res.json()
        print("接口返回结果：" + json.dumps(res_json))
        assert res_json['resultCode'] == 200
        assert res_json['data']['list'] is not None
        assert res_json['data']['list'][0]['orderId'] is not None

