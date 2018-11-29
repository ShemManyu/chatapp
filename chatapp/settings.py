# -*- coding: utf-8 -*-
"""Application configuration.

Most configuration is set via environment variables.

For local development, use a .env file to set
environment variables.
"""
import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

#ENV = env.str('FLASK_ENV', default='production')
#DEBUG = ENV == 'development'

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'.format(
        DB_PASSWORD=os.getenv("DB_PASSWORD", "postgres"),
        DB_USER = os.getenv("DB_USER", "postgres"),
        DB_HOST = os.getenv("DB_HOST", "localhost"),
        DB_NAME = os.getenv("DB_NAME", "postgres")
    )

SECRET_KEY = os.getenv("SECRET_KEY", 'default')

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")

GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")

BCRYPT_LOG_ROUNDS = os.getenv('BCRYPT_LOG_ROUNDS', 13)
DEBUG_TB_ENABLED = True #check this baadaye
DEBUG_TB_INTERCEPT_REDIRECTS = False
CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
SQLALCHEMY_TRACK_MODIFICATIONS = False
WEBPACK_MANIFEST_PATH = 'webpack/manifest.json'
