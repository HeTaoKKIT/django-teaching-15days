
SUCCESS = {'code': 200, 'msg': '请求成功'}
DATABASE_ERROR = {'code': 500, 'msg': '数据库崩了'}

# 用户模块
USER_REGISTER_CODE_ERROR = {'code': 1000, 'msg': '验证码错误'}
USER_REGISTER_PARAMS_VALID = {'code': 1001, 'msg': '请填写完整的注册参数'}
USER_REGISTER_MOBILE_INVALID = {'code': 1002, 'msg': '手机格式不正确'}
USER_REGISTER_PASSWORD_ERROR = {'code': 1003, 'msg': '两次密码不正确'}
USER_REGISTER_MOBILE_EXSIST = {'code': 1004, 'msg': '手机号已存在，请登录'}

USER_LOGIN_PARAMS_VALID = {'code': 1005, 'msg': '请填写完整的登录信息'}
USER_LOGIN_PASSWORD_INVALID = {'code': 1006, 'msg': '登录密码不正确'}
USER_LOGIN_PHONE_INVALID = {'code': 1007, 'msg': '请填写正确的手机号'}
