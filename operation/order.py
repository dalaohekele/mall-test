#  -*-  coding:utf-8 -*-
from core.result_base import ResultBase
from api.order import order


def get_order_list(status):
    """
    获取订单列表
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    res = order.order_list(status)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
    result.msg = res.json()["msg"]
    result.response = res
    return result
