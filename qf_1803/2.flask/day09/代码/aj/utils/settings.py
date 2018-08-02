
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

static_folder = os.path.join(BASE_DIR, 'static')

template_folder = os.path.join(BASE_DIR, 'templates')

# 上传图片地址
media_folder = os.path.join(static_folder, 'media')
upload_folder = os.path.join(media_folder, 'upload')

MYSQL_DATABASE = {
    'USER':'root',
    'PASSWORD':'123456',
    'HOST':'127.0.0.1',
    'PORT':3306,
    'DB':'aj3',
    'ENGINE':'mysql',
    'DRIVER':'pymysql'
}

REDIS_DATABASE = {
    'HOST':'127.0.0.1',
    'PORT': 6379
}
