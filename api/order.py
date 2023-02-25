#  -*-  coding:utf-8 -*-
import os
from core.rest_client import RestClient
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]


class Order(RestClient):

    def __init__(self, api_root_url, **kwargs):
        super(Order, self).__init__(api_root_url, **kwargs)

    def order_list(self, status, **kwargs):
        return self.get("/api/v1/order?pageNumber=1&status={}", status, **kwargs)


order =Order(api_root_url)