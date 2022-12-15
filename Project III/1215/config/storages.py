import os
from abc import ABC
from tempfile import SpooledTemporaryFile
from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage, ABC):
    # 커스텀 경로
    # 아래 작성한 경로 하위로 media 파일이 저장
    # 예시
    # location = "custom_media_path"
    location = "media"

    """
    This is our custom version of S3Boto3Storage that fixes a bug in
    boto3 where the passed in file is closed upon upload.
    From:
    https://github.com/matthewwithanm/django-imagekit/issues/391#issuecomment-275367006
    https://github.com/boto/boto3/issues/929
    https://github.com/matthewwithanm/django-imagekit/issues/391
    https://github.com/jschneier/django-storages/issues/382#issuecomment-674914649
    https://ysde.blogspot.com/2020/03/djangodjango-storages-upload-to-s3.html
    """

    def _save(self, name, content):
        """
        We create a clone of the content file as when this is passed to
        boto3 it wrongly closes the file upon upload where as the storage
        backend expects it to still be open
        """
        # Seek our content back to the start
        content.seek(0, os.SEEK_SET)

        # Create a temporary file that will write to disk after a specified
        # size. This file will be automatically deleted when closed by
        # boto3 or after exiting the `with` statement if the boto3 is fixed
        with SpooledTemporaryFile() as content_autoclose:

            # Write our original content into our copy that will be closed by boto3
            content_autoclose.write(content.read())

            # Upload the object which will auto close the
            # content_autoclose instance
            return super(MediaStorage, self)._save(name, content_autoclose)
