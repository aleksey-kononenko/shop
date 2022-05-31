DEBUG = False
ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "db_shop",
        'USER': "alex",
        'PASSWORD': "marik2010",
        'HOST': "localhost",
        'PORT': "",  # 5432 by default
    }
}