import os

PATH_CONST__CWD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PATH_CONST__LOCAL_SETTINGS_FILE = os.path.join(PATH_CONST__CWD, 'local.service-secrets.json')
