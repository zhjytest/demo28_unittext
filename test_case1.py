
# 导包
from controller import login



# 测试

# 比较 ： 预期结果 == 实际结果

# assert : 断言

# case1 : 验证正确的用户名和密码进行登陆
assert "登陆成功" == login('admin','123456')

# case2 : 验证正确的用户名和空的密码
assert  "密码不能为空!" == login('admin','')

assert "登陆成功" == login('admin','123456')



