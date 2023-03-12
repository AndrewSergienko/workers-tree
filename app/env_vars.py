import os

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = os.getenv("DEBUG") == "TRUE"

ALLOWED_HOSTS = ["127.0.0.1", os.getenv("ALLOWED_HOST")]
