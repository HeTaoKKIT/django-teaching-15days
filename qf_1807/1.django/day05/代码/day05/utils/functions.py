
import random


def get_cookie_token():
    s = '1234567890qwertyuiopasdfghjklzxcvbnm'
    token = ''
    for i in range(20):
        token += random.choice(s)
    return token
