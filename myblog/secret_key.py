
from config_app.infra.path_const import PATH_CONST__LOCAL_SETTINGS_FILE
from config_app.infra.secrets import Secrets


_secrets = Secrets.from_file(PATH_CONST__LOCAL_SETTINGS_FILE)


SECRET__SECRET_KEY = _secrets.ensure_secret('SECRET_KEY')
SECRET__APP_DB__DB_NAME = _secrets.ensure_secret('POSTGRES_DB')
SECRET__APP_DB__USER = _secrets.ensure_secret('POSTGRES_USER')
SECRET__APP_DB__PASSWORD = _secrets.ensure_secret('POSTGRES_PASSWORD')