DEBUG = False
ALLOWED_HOSTS = ['localhost', '137.184.2.173']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "eShop",
        'USER': "eShop",
        'PASSWORD': "marik2010",
        'HOST': "localhost",
        'PORT': "",  # 5432 by default
    }
}