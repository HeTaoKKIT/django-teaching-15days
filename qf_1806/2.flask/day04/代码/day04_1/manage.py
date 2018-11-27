
import pymysql

from flask import Flask, g

app = Flask(__name__)


@app.route('/hello/')
def hello():
    # 获取学生表中的数据
    sql = 'select * from student;'
    result = g.cursor.execute(sql)
    data = g.cursor.fetchall()
    return 'hello world'


@app.before_request
def before_request():
    # TODO： pymysql连接数据库
    conn = pymysql.Connection(host='127.0.0.1', port=3306,
                              user='root', password='123456',
                              database='flask6')
    # 游标
    cursor = conn.cursor()
    g.cursor = cursor
    g.conn = conn
    # corsor.execute(sql)
    print('数据库在此方法中进行连接')


@app.teardown_request
def teardown_request(exception):
    # 关闭数据库的链接
    g.conn.close()


if __name__ == '__main__':
    app.run()




