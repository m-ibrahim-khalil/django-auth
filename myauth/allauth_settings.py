"""
    * Allauth Settings
    * General Account Settings
"""

from dotenv import load_dotenv
import os

load_dotenv()


ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_VERIFICATION = "optional"
LOGIN_REDIRECT_URL = "/profile"
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False

# ACCOUNT_USER_MODEL_USERNAME_FIELD = None
# ACCOUNT_SESSION_REMEMBER = False
# ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
# ACCOUNT_EMAIL_SUBJECT_PREFIX = '[Site] '
# ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = False


"""
    * Social Account Settings
"""

SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "APPS": [
            {
                "client_id": os.getenv("GOOGLE_CLIENT_ID"),
                "secret": os.getenv("GOOGLE_CLIENT_SECRET"),
                "key": "",
            },
        ],
        "SCOPE": [
            "profile",
            "email",
        ],
    }
}
SOCIALACCOUNT_EMAIL_AUTHENTICATION = True
SOCIALACCOUNT_EMAIL_AUTHENTICATION_AUTO_CONNECT = True
# SOCIALACCOUNT_AUTO_SIGNUP = False
# SOCIALACCOUNT_AVATAR_SUPPORT
