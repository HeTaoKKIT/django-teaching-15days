
import time
import logging

from django.utils.deprecation import MiddlewareMixin

# 获取logger
log = logging.getLogger(__name__)


class LogMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # 绑定在request上一个属性，表示访问的时间
        request.init_time = time.time()

    def process_response(self, request, response):
        # 请求URL耗时时间
        count_time = time.time() - request.init_time
        # 响应状态码
        code = response.status_code
        # 请求地址
        path = request.path
        # 请求方法
        method = request.method
        # 响应内容
        content = response.content
        # 需要打印的日志信息
        log_str = '%s %s %s %s %s' % (path, method, code,
                                      count_time, content)
        # 交给logger处理日志
        log.info(log_str)
        return response
