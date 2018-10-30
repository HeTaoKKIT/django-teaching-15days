
import time
import logging
from django.utils.deprecation import MiddlewareMixin


class TestMiddleware(MiddlewareMixin):

    def process_request(self, request):
        print('process_request1')
        # 继续执行对应的视图函数
        return None

    def process_response(self, request, response):
        print('process_response1')
        # 返回响应
        return response


class Test2Middleware(MiddlewareMixin):

    def process_request(self, request):
        print('process_request2')
        # 继续执行对应的视图函数
        return None

    def process_response(self, request, response):
        print('process_response2')
        # 返回响应
        return response


class LoggingMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # 记录当前请求访问服务器的时间，请求参数，请求内容....
        request.init_time = time.time()
        request.init_body = request.body
        return None

    def process_response(self, request, response):
        try:
            # 记录返回响应的时间和访问服务器的时间的差，记录返回状态码....
            times = time.time() - request.init_time
            # 响应状态码
            code = response.status_code
            # 响应内容
            res_body = response.content
            # 请求内容
            req_body = request.init_body
            # 日志信息
            msg = '%s %s %s %s' % (times, code, res_body, req_body)
            # 写入日志
            logging.info(msg)
        except Exception as e:
            logging.critical('log error, Exception: %s' % e)
        return response



