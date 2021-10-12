import unittest
from controller import  login



class TestLogin(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls) -> None:
    #     print("开始执行测试用例")
    #
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print("测试用例执行完毕")
    #
    #
    # # 初始化方法
    # def setUp(self) -> None:
    #     print("执行初始化工作")
    #
    #
    # # 清空方法
    # def tearDown(self) -> None:
    #     print("执行清空工作")


    # case1 : 验证正确的用户名和密码进行登陆
    @unittest.skip("此测试用例正在开发中，暂时不执行")
    def test_login1(self):
        print("执行测试用例1")
        self.assertEqual("登陆成功",login('admin','123456'))


    # case2 : 验证正确的用户名和空的密码
    def test_login2(self):
        print("执行测试用例2")
        self.assertEqual("用户名不能为空",login('','123456'))


    # case3 : 验证密码不为空
    def test_login3(self):
        print("执行测试用例3")
        self.assertEqual("密码为空",login('admin',''))



# suite = unittest.TestSuite()
# #suite.addTest(TestLogin('test_login2'))
# #suite.addTest(TestLogin('test_login3'))
#
# case_list = [TestLogin('test_login2'),TestLogin('test_login3')]
#
# suite.addTests(case_list)
#
# runner = unittest.TextTestRunner(verbosity=2)
# runner.run(suite)

# suite_smoke = unittest.TestSuite()
# suite_smoke.addTest(TestLogin('test_login1'))
