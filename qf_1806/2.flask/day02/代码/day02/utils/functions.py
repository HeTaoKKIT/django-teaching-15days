
from flask import session, redirect, url_for


def is_login(func):
    def check():
        try:
            user_id = session['user_id']
        except Exception as e:
            return redirect(url_for('user.login'))
        return func()
    return check


def login_required(func):
    def check():
        user_id = session.get('user_id')
        if not user_id:
            return redirect(url_for('user.login'))
        return func()
    return check
