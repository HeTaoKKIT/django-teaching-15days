
import random


def random_ticket():
    s = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    ticket = ''
    for i in range(100):
        ticket += random.choice(s)
    return ticket



