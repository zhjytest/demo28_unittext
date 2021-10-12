import unittest
from HTMLTestRunner import HTMLTestRunner


# 所有的测试用例都从该入口去运行 ，从这个里面去组装套件，然后运行套件

# 1. 创建套件
suite = unittest.TestLoader().discover(r'E:\project\demo28_unittext',pattern='test*.py')


# 生成文件
report_path = 'test_report.html'
with open(report_path,'wb') as f:
    runner = HTMLTestRunner(f,title='测试报告',description='v1.0')
    runner.run(suite)
