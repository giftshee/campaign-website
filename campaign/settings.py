"""
Django settings for campaign project.
"""

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent


# ================= SECURITY =================

SECRET_KEY = 'django-insecure-!-5e=^ikd3l4cp#6e*l@%6ruifu1tm3g^4of=tgs1huy=+&cf='

DEBUG = True

ALLOWED_HOSTS = ["*"]


# ================= APPLICATIONS =================

INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Cloudinary
    'cloudinary',
    'cloudinary_storage',

    # Your app
    'website',
]


# ================= MIDDLEWARE =================

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',

    # WhiteNoise for static files
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]


# ================= URLS =================

ROOT_URLCONF = 'campaign.urls'


# ================= TEMPLATES =================

TEMPLATES = [

    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [
            BASE_DIR / 'website/templates'
        ],

        'APP_DIRS': True,

        'OPTIONS': {

            'context_processors': [

                'django.template.context_processors.request',

                'django.contrib.auth.context_processors.auth',

                'django.contrib.messages.context_processors.messages',

            ],

        },

    },

]


WSGI_APPLICATION = 'campaign.wsgi.application'


# ================= DATABASE =================

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.sqlite3',

        'NAME': BASE_DIR / 'db.sqlite3',

    }

}



# ================= PASSWORD VALIDATION =================

AUTH_PASSWORD_VALIDATORS = [

    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },

]



# ================= LANGUAGE =================

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_TZ = True



# ================= CLOUDINARY MEDIA STORAGE =================

import cloudinary

cloudinary.config(

    cloud_name=os.environ.get(
        "CLOUDINARY_CLOUD_NAME"
    ),

    api_key=os.environ.get(
        "CLOUDINARY_API_KEY"
    ),

    api_secret=os.environ.get(
        "CLOUDINARY_API_SECRET"
    )

)


# Send all uploads to Cloudinary

DEFAULT_FILE_STORAGE = (
    "cloudinary_storage.storage.MediaCloudinaryStorage"
)



# ================= STATIC FILES =================

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"


STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)



# ================= LOGIN =================

LOGIN_URL = '/admin/login/'



# ================= DEFAULT FIELD =================

DEFAULT_AUTO_FIELD = (
    'django.db.models.BigAutoField'
)