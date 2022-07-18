DEBUG = False
ALLOWED_HOSTS = ['*',]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "eShop",
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': "localhost",
        'PORT': "",  # 5432 by default
    }
}