
### 注册接口

#### 请求request

    POST /user/register/

#### 请求参数

    mobile str 手机号
    imagecode str 图片验证码
    passwd str 密码
    passwd2 str 确认密码

#### 响应response

    {'code': 1000, 'msg': '请填写完整的参数'}
    {'code': 1001, 'msg': '手机号不符合规范'}
    {'code': 200, 'msg': '请求成功'}

#### 响应参数

    code int 状态码
    msg str 返回信息