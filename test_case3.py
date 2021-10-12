import unittest
from controller import  login
from parameterized import parameterized


class TestLogin(unittest.TestCase):


    @parameterized.expand([("登陆成功","admin","123456"),("用户名不能为空",'','123456'),("密码不能为空","admin",'')])
    def test_login(self,expect,username,password):
        self.assertEqual(expect,login(username,password))




    # # case1 : 验证正确的用户名和密码进行登陆
    # def test_login1(self):
    #     print("执行测试用例1")
    #     self.assertEqual("登陆成功",login('admin','123456'))
    #
    #
    # # case2 : 验证正确的用户名和空的密码
    # def test_login2(self):
    #     print("执行测试用例2")
    #     self.assertEqual("用户名不能为空",login('','123456'))
    #
    #
    # # case3 : 验证密码不为空
    # def test_login3(self):
    #     print("执行测试用例3")
    #     self.assertEqual("密码为空",login('admin',''))


