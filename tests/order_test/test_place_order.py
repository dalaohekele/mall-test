#  -*-  coding:utf-8 -*-
import requests
import json


class TestPlaceOrder():
    # 接口下单流程：加载商详->快速购买->加载购物车->获取收货地址->提交订单
    def test_place_order(self):
        goods_id = 10283
        host = 'http://localhost:8888'
        header = {'token': 'e6b0b3fc417cd19dc8930165065cf57c'}
        # 商详接口
        goods_path = '/api/v1/goods/detail/' + str(goods_id)
        goods_detail_res = requests.request('GET', url=host + goods_path, headers=header, params=None)
        goods_detail_res_json = goods_detail_res.json()
        print("商详接口返回结果：" + json.dumps(goods_detail_res_json))
        assert goods_detail_res_json['resultCode'] == 200
        assert goods_detail_res_json['data']['goodsId'] == goods_id
        # 购买商品
        shop_cart_path = '/api/v1/shop-cart'
        shop_cart_index_res = requests.request('GET', url=host + shop_cart_path, headers=header, params=None)
        print("购物车接口返回结果：" + json.dumps(shop_cart_index_res.json()))

        shop_params = {'goodsCount': 1, 'goodsId': goods_id}
        shop_cart_res = requests.request('POST', url=host + shop_cart_path, headers=header, json=shop_params)
        shop_cart_res_json = shop_cart_res.json()
        print("购买商品接口返回结果：" + json.dumps(shop_cart_res_json))
        assert shop_cart_res_json['resultCode'] == 200
        # 加载购物车
        user_cart_res = requests.request('GET', url=host + shop_cart_path, headers=header, params=None)
        user_cart_res_json = user_cart_res.json()
        print("加载购物车接口返回结果：" + json.dumps(user_cart_res_json))
        assert user_cart_res_json['resultCode'] == 200
        assert user_cart_res_json['data'][0]['goodsId'] == goods_id
        cart_item_id = user_cart_res_json['data'][0]['cartItemId']
        # 购物车算价
        settle_path = '/api/v1/shop-cart/settle?cartItemIds=' + str(cart_item_id)
        settle_res = requests.request('GET', url=host + settle_path, headers=header, params=None)
        settle_res_json = settle_res.json()
        print("购物车算价接口返回结果：" + json.dumps(settle_res_json))
        assert settle_res_json['resultCode'] == 200
        # 收货地址
        user_address_path = '/api/v1/address/default'
        address_res = requests.request('GET', url=host + user_address_path, headers=header, params=None)
        address_res_json = address_res.json()
        print("收货地址接口返回结果：" + json.dumps(address_res_json))
        assert address_res_json['resultCode'] == 200
        assert address_res_json['data']['addressId'] is not None
        address_id = address_res_json['data']['addressId']
        # 提交订单
        save_order_path = '/api/v1/saveOrder'
        save_params = {"addressId": address_id, "cartItemIds": [cart_item_id]}
        save_order_res = requests.request('POST', url=host + save_order_path, headers=header, json=save_params)
        save_order_res_json = save_order_res.json()
        print("提交订单接口返回结果：" + json.dumps(save_order_res_json))


if __name__ == '__main__':
    TestPlaceOrder().test_place_order()
