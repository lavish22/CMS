from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    bucket_name = 'wagtailcms'
    


#/Users/shahzeb/.local/share/virtualenvs/shahzeb-ILVeH350/lib/python3.8    -- change in python.pythonPath