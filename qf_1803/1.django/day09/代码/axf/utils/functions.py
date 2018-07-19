
import random
from datetime import datetime


def get_ticket():
    ticket = ''
    s = 'qwertyuioplkjhgfdsazxcvbnm1234567890'
    for i in range(100):
        ticket += random.choice(s)
    return ticket


def get_order_num():
    num = ''
    s = 'qwertyuioplkjhgfdsazxcvbnm1234567890'
    for i in range(10):
        num += random.choice(s)
    order_time = datetime.now().strftime('%Y%m%d%H%M%S')
    return order_time + num
