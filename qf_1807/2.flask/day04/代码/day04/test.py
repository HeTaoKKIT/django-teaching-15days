
from flask import Flask, abort
from werkzeug.routing import Rule,Map,MapAdapter,BaseConverter
app = Flask(__name__)

@app.route('/')
def index():
    print('index run---')
    abort(404)
    return 'hello world'

# 请求钩子：四种，两种在请求前执行，两种在请求后执行

# 请求前执行
# before_first_request在第一次请求前执行，只执行一次。
@app.before_first_request
def befor_firt_request():
    print('before first request run---')

# 在每次请求前都执行
@app.before_request
def before_request():
    print('before request run---')

# 请求后执行
# after_request:没有异常的情况下，在每次请求后执行，接收的参数为响应对象
@app.after_request
def after_request(response):
    print('after request run---')
    # 修改响应的类型
    response.headers['Content-Type'] = 'application/json'
    return response

# teardown_request：即使有异常，在每次请求后执行，接收的参数为异常信息
@app.teardown_request
def teardown_reqeust(e):
    print('teardown request run---')


# 异常：可以通过手动触发实现异常吗？abort(400)
# 异常到底是指什么异常？

if __name__ == '__main__':
    # print(app.url_map)
    app.run(debug=True)
