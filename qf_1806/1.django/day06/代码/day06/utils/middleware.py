
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


