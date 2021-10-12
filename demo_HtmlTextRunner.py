

# 1. 放在当前的项目下 ，为了导包


# 2.导入 HTMLTestRunner 类
"""
就是把unittest.TextTestRunner做了一个加强 ，主要是把测试结果写到了一个html文件中，
但是保留了TextTestRunner的run方法
"""
from HTMLTestRunner import HTMLTestRunner

# 3. 使用run方法，写到了html里面

flname = 'test_report.html'
f = open(flname,'wb')

runner = HTMLTestRunner(f,title='测试报告',description='v1.0')
runner.run(suite)

f.close()


# 关键字 ： with
with open(flname,'wb') as f:
    runner = HTMLTestRunner(f, title='测试报告', description='v1.0')
    runner.run(suite)