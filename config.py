from os import getenv , path
from dotenv import load_dotenv

SECRET_KEY = getenv("SECRET_KEY")
DB_NAME = getenv("DB_NAME")
DB_USERNAME = getenv("DB_USERNAME")
DB_PASSWORD = getenv("DB_PASSWORD")
DB_HOST = getenv("DB_HOST")
CLOUD_NAME=getenv("CLOUD_NAME")
API_KEY=getenv("API_KEY")
API_SECRET=getenv("API_SECRET")
BOOTSTRAP_SERVE_LOCAL = getenv("BOOTSTRAP_SERVE_LOCAL")