#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# from pytest_html.plugin import HTMLReport
# import HTMLTestReport
import Common.HTMLTestRunner as HTMLTestRunner
import getpathInfo
import getUrlParams
import readConfig
import readExcel
from Common.configEmail import SendEmail
from apscheduler.schedulers.blocking import BlockingScheduler
# import pythoncom
import unittest
import Common.Log
import threading
from Common.tomorrow import threads
import time

LOG = Common.Log.logger
SEND_EMAIL = SendEmail(
    username='xyyy1227@163.com',
    passwd='LOKYDYYSTTZVCKMU',
    recv=['692707223@qq.com', '1830606425@qq.com'],
    title='xy163EmailTest',
    content='测试发送邮件',
    file=r'/Users/xy/PycharmProjects/pythonProject/xiaoya/cs/result/report.html',
    ssl=True,
)
PATH = getpathInfo.get_path()
REPORT_PATH = os.path.join(PATH, 'result')
ON_OFF = readConfig.ReadConfig().get_email('on_off')

class AllTest():
    def __init__(self):
        global RESULT_PATH
        RESULT_PATH = os.path.join(REPORT_PATH, 'report.html')
        self.caseListFile = os.path.join(PATH, 'caselist.txt')
        self.caseFile = os.path.join(PATH, 'testCase')
        self.caseList = []

    def set_case_list(self):
        """
        读取caselist.txt中的测试用例，并添加进caseList列表中
        :return:
        """
        fb = open(self.caseListFile)
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith('#'): #如果data非空且不以#开头
                self.caseList.append(data.replace('\n', ''))
        fb.close()

    def set_case_suite(self):
        """
        :return:
        """
        self.set_case_list()  # 通过set_case_list()拿到caselist元素组
        test_suite = unittest.TestSuite()
        suite_module = []
        threads = []
        for case in self.caseList:  # 从caselist元素组中循环取出case
            case_name = case.split("/")[-1]  # 通过split函数来将aaa/bbb分割字符串，-1取后面，0取前面
            print(case_name + ".py")  # 打印出取出来的名称
            # 批量加载用例，第一个参数为用例存放路径，第一个参数为路径文件名
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name + '.py',
                                                           top_level_dir=None)
            suite_module.append(discover)  # 将discover存入suite_module元素组
            print('suite_module:' + str(suite_module))
        if len(suite_module) > 0:  # 判断suite_module元素组是否存在元素
            for suite in suite_module:  # 如果存在，循环取出元素组内容，命名为suite
                for test_name in suite:  # 从discover中取出test_name，使用addTest添加到测试集
                    test_suite.addTest(test_name)
                # for test_name in suite:  # 从discover中取出test_name，使用addTest添加到测试集
                #     # 多线程
                #     print("multi_thread begin")
                #     threads.append(threading.Thread(target=test_suite.addTest, args=(test_name)))
                #
                # for thread in threads:
                #     thread.start()
                #
                # for thread in threads:
                #     thread.join()
                # print("multi_thread end")
        else:
            print('else:')
            return None
        print(test_suite)
        return test_suite  # 返回测试集

    @threads(10) #多线程
    def run_case(self, suit):
        now = time.strftime('%Y-%m-%d %H-%M-%S')
        report_file = os.path.join(REPORT_PATH, now + 'report.html')
        fp = open(report_file, 'wb')  # 打开result/report.html测试报告文件，如果不存在就创建
        # 调用HTMLTestRunner
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report',
                                               description='Test Description')
        # runner = HTMLReport.TestRunner(
        #     title="XXX项目测试报告",
        #     description="测试人员：CesareCheung",
        #     report_file_name=f"testreport",
        #     thread_count=50
        # )
        runner.run(suit)

    def run(self, suit, SEND_MAIL=None):
        """
        run test
        :return:
        """
        t1 = time.time()
        try:
            print('try')
            print(str(suit))
            if suit is not None:  # 判断test_suite是否为空
                print('if-suit')
                self.run_case(suit)
                t2 = time.time()
                print('end:%s' % time.ctime())
                print('总共花费时间:%s' % (t2 - t1))
            else:
                print("Have no case to test.")
        except Exception as ex:
            print(str(ex))
            LOG.info(str(ex))

        finally:
            print("*********TEST END*********")
            LOG.info("*********TEST END*********")
            # fp.close()
        # 判断邮件发送的开关
        if ON_OFF == 'on':
            SEND_EMAIL.send_email()
        else:
            print("邮件发送开关配置关闭，请打开开关后可正常自动发送测试报告")



# pythoncom.CoInitialize()
# scheduler = BlockingScheduler()
# scheduler.add_job(AllTest().run, 'cron', day_of_week='1-5', hour=14, minute=59)
# scheduler.start()


if __name__ == '__main__':
    # 调用set_case_suite获取test_suite
    cases = AllTest()
    for suit in cases.set_case_suite():
        print(suit, type(suit))
        AllTest().run(suit)







