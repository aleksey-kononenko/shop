DEBUG = False
ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db1',
        'USER': 'eCommerce',
        'PASSWORD': 'marik2010',
        'HOST': 'localhost',
        'PORT': '',
    }
}