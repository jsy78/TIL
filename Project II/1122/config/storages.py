from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    # 커스텀 경로
    # 아래 작성한 경로 하위로 media 파일이 저장
    # 예시
    # location = "custom_media_path"
    location = "media"
