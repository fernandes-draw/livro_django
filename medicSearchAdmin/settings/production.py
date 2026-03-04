from .settings import *

DEBUG = False

# Crie a secret key para seu ambiente de desenvolvimento
SECRET_KEY = "ixb62ha#ts=ab4t2u%p1_62-!5w2j==j6d^3-j$!z(@*m+-h"

# Alterar para o ip do ambiente de produção quando houver.
ALLOWED_HOSTS = ["127.0.0.1"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# =========== PostgreSQL ===========

# (venv)  pip install psycopg2

# DATABASES = {
#  'default': {
#  'ENGINE': 'django.db.backends.postgresql_psycopg2',
#  'NAME': 'Nome do seu banco de dados',
#  'USER': 'Nome do usuário',
#  'PASSWORD': 'Senha',
#  'HOST': 'Nome do host de conexão ao banco',
#  'PORT': 'Número da porta de comunicação',
#  }
# }

# ========== MariaDB ou MySQL ================

# (venv)  pip install mysqlclient

# DATABASES = {
#     'default': {
#     'ENGINE': 'django.db.backends.mysql',
#     'NAME': 'Nome do seu banco de dados',
#     'USER': 'Nome do usuário',
#     'PASSWORD': 'Senha',
#     'HOST': 'Nome do host de conexão ao banco',
#     'PORT': 'Número da porta de comunicação',
#     }
# }

# ========= SQLServer ==============

# (venv)  pip install django-pyodbc-azure

# DATABASES = {
#     'default': {
#     'ENGINE': 'sql_server.pyodbc',
#     'NAME': 'Nome do seu banco de dados',
#     'USER': 'Nome do usuário',
#     'PASSWORD': 'Senha',
#     'HOST': 'Nome do host de conexão ao banco',
#     'PORT': 'Número da porta de comunicação',
#     },
# }


# =============== Oracle ===================

# DATABASES = {
#     'default': {
#     'ENGINE': 'django.db.backends.oracle',
#     'NAME': 'Nome do seu banco de dados',
#     'USER': 'Nome do usuário',
#     'PASSWORD': 'Senha',
#     'HOST': '',
#     'PORT': '',
#     }
# }
