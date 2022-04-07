import unittest
from BeautifulReport import BeautifulReport
from iwebsns.config.config import *

cases = unittest.defaultTestLoader.discover(start_dir=case_path, pattern='test*.py')
result = BeautifulReport(cases)
result.report(description='登录的测试报告', filename='第一轮测试结果', report_dir=result_path)
