import dj_database_url
DEBUG = False

ALLOWED_HOSTS = ['*']

db_from_env = dj_database_url.config()

DATABASES['default'].update(db_from_env)
