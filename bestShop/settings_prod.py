DEBUG = False
ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresq1_psycopg2',
        'NAME': 'db1',
        'USER': 'eCommerce',
        'PASSWORD': 'marik2010',
        'HOST': 'localhost',
        'PORT': '',
    }
}