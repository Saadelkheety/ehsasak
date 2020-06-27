from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'great secret key')

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['127.0.0.1', '138.197.6.134', 'beldezign.us', 'www.beldezign.us']

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'maprabusiness@gmail.com'
EMAIL_HOST_PASSWORD = 'M87654321'
EMAIL_PORT = 587

try:
    from .local import *
except ImportError:
    pass
