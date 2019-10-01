import os

APP_HOST = os.getenv('APP_HOST')
APP_PORT = os.getenv('APP_PORT')

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

JSONSCHEMA_PATH = os.getenv('JSONSCHEMA_PATH', '/app/jsoncheme/increment/request.json')
