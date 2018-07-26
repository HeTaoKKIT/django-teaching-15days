
from functools import wraps
from flask import session, redirect, url_for


def is_login(func):
    @wraps(func)
    def check_login(*args, **kwargs):
        if 'user_id' in session:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('first.new_login'))
    return check_login

