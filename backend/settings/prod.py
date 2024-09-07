from .dev import *
import dj_database_url

SECURE_SSL_REDIRECT = True  # [1]
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

DEBUG = True

print("Looking for production database.")
DB_URL = os.getenv("DATABASE_URL")
print(f"Found DB_URL: {DB_URL}")
DATABASES["default"] = dj_database_url.config(
    conn_max_age=600, ssl_require=True, default=DB_URL
)

SECRET_KEY = "rb@&a^^7$7#f7c*e*^+55&sknu6g!f+2zuh09bagm2#veitcg0"
