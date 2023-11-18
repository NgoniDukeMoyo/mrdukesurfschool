if 'USE_AWS' in os.enviro:
    #bucket config
    AWS_STORAGE_BUCKET_NAME = 'surfschoolobjects'
    AWS_S3_REGION_NAME = 'Europe (Stockholm) eu-north-1'
    AWS_ACCESS_KEY_ID = 'AKIARJC22ZQCXSPPFAMW'
    AWS_SECRET_ACCESS_KEY = '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'
    AWS_S3_CUSTOM_DOMAIN_NAME = f'{ AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'