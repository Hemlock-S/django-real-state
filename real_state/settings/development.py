from .base import *

DATABASES = {
    'default': {
        'ENGINE': env('POSTGRES_ENGINE'),  # Matches .env variable
        'NAME': env('POSTGRES_DB'),        # Matches .env variable
        'USER': env('POSTGRES_USER'),      # Matches .env variable
        'PASSWORD': env('POSTGRES_PASSWORD'),  # Matches .env variable
        'HOST': env('PG_HOST'),            # Matches .env variable
        'PORT': env('PG_PORT'),            # Matches .env variable
    }
}