
import random
from datetime import datetime


def random_ticket():
    s = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    ticket = ''
    for i in range(100):
        ticket += random.choice(s)
    return ticket


def get_order_number():
    s='1234567890'
    o_num = ''
    for i in range(20):
        o_num += random.choice(s)
    o_num += datetime.now().strftime('%Y%m%d%H%M%S')
    return o_num




