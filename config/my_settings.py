# import pymysql
# pymysql.install_as_MySQLdb()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'knu_db',
        'USER': 'root',
        'PASSWORD': 'Sangju00!',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}