STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

MEDIA_URL = '/mdeia/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

if 'USE_AWS' in os.enviro:
    #bucket config
    AWS_STORAGE_BUCKET_NAME = 'mrdukesurfschoollatest'
    AWS_S3_REGION_NAME = 'Europe (Stockholm) eu-north-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN_NAME = f'{ AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    #other
    'storages'
