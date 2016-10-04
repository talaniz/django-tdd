from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../database/db-auth.sqlite3'), # Different database
    }
}

# New variable for our authtools backend
AUTH_USER_MODEL = 'authtools.User'
