#  -*-  coding:utf-8 -*-
from operation.order import get_order_list


class TestOrderList():
    def test_order_list_all(self):
        result = get_order_list(stauts='')
        assert result['resultCode'] == 200
        assert result['data']['list'] is not None
        assert result['data']['list'][0]['orderId'] is not None
