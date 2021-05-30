#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import unittest
from Common.configHttp import RunMain
import paramunittest
import getUrlParams
import urllib.parse
import readExcel
import Common.Log

LOG = Common.Log.logger
URL = str(getUrlParams.GetUrlParams().get_url())
login_xls = readExcel.readExcel().get_xls('userCase.xlsx', 'login')

@paramunittest.parametrized(*login_xls)
class TestUserLogin(unittest.TestCase):
    def setParameters(self, case_name, path, query, method):
        """
        set params
        :param case_name:
        :param path:
        :param query:
        :param method:
        :return:
        """
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)
        LOG.info(self.method)
        LOG.info(self.path)

    def desription(self):
        """
        test report description
        :return:
        """
        self.case_name

    def setUp(self) -> None:
        """
        :return:
        """
        print(self.case_name+"测试开始前准备")

    def test01case(self):
        """
        check test result
        :return:
        """
        url1 = "http://www.XXX.com/login?"
        data_url = url1 + self.query
        # 将一个完整的URL中的name=&pwd=转换为{'name':'xxx','pwd':'bbb'}
        data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(data_url).query))
        LOG.info(type(self.method))
        LOG.info(type(URL))
        LOG.info(type(data1))
        RunMain().run_main(self.method, URL, data1)
        LOG.info(RunMain().run_main(self.method, URL, data1))
        info = RunMain().run_main(method=str(self.method), url=str(URL), data=dict(data1))
        LOG.info(info)
        res = json.loads(info)
        if self.case_name == 'login_right':
            self.assertEqual(res['code'], 200)
        if self.case_name == 'login_error':
            self.assertEqual(res['code'], -1)
        if self.case_name == 'login_null':
            self.assertEqual(res['code'], 10001)
