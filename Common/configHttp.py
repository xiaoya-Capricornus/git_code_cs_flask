#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json


class RunMain():

    def send_post(self, url, data):
        #canshu
        # result = requests.post(verify=False, url=url, data=data).json()
        result = requests.post(url=url, data=data).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def send_get(self, url, data):
        result = requests.get(url=url, params=data).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def run_main(self, method, url=None, data=None):
        result = None
        if method == 'post':
            result = self.send_post(url, data)
            print(data)
        elif method == 'get':
            result = self.send_get(url, data)
        else:
            print("The value of method is error!")
        return result


if __name__ == '__main__':
    method_post = 'post'
    url_post = 'http://127.0.0.1:9999/login'
    # data_post = '123'
    data_post = {'name': 'xiaoya', 'pwd': '123456'}
    result_run_main_post = RunMain().run_main(method=method_post, url=url_post, data=data_post)
    print(result_run_main_post)
    method_get = 'get'
    url_get = 'http://127.0.0.1:9999/login'
    params_get = {'name': 'xiaoya', 'pwd': '123456'}
    result_run_main_get = RunMain().run_main(method=method_get, url=url_get, data=params_get)
    print(result_run_main_get)
    # # result1 = RunMain().run_main('post', 'http://127.0.0.1:9999/login', {'name': 'xiaoming','pwd':'111'})
    # result2 = RunMain().run_main('get', 'http://127.0.0.1:9999/login', 'name=xiaoming&pwd=111')
    # # print(result1)
    # print(result2)
