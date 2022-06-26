from pickle import TRUE
from .base import *
from .base import env

DEBUG = TRUE
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY",default='django-insecure-)12^_9d9=-bj=f5bz*etb0+mwu@zgp+unl884fm&64lhsq3byx',)


ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]