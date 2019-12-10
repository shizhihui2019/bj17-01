import unittest
from tools.HTMLTestReportCN import HTMLTestRunner

# 定义测试套件
suite = unittest.defaultTestLoader.discover("./scripts")


# 获取报告存储文件流 并 实例化 HTMTestRunner 调用run方法
with open("./report/report.html","wb") as f:
    HTMLTestRunner(stream=f).run(suite)

# 老师查错测试代码
# unittest.TextTestRunner().run(suite)
