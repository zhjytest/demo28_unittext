


# 实现登陆功能
def login(username,password):

    if username is None or username == '':
        return "用户名不能为空"
    if password is None or password == '':
        return  "密码不能为空"

    if username == 'admin' and password == '123456':
        return "登陆成功"
    else:
        return "登陆失败"