
import logging
logger = logging.getLogger('dj')


def print_log(func):

    def logs(request):
        logger.info('hello')
        return func(request)

    return logs
