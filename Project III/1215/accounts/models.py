from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from multiselectfield import MultiSelectField
from imagekit.processors import Thumbnail, Transpose

# Create your models here.
# 이름 비밀번호 설명 주소 생년월일


class User(AbstractUser):
    GENDER_CHOICES = (
        ("M", "남자"),
        ("F", "여자"),
    )
    gender = models.CharField(  # 성별
        max_length=2,
        choices=GENDER_CHOICES,
    )
    address = models.CharField(max_length=50)  # 주소
    address_detail = models.CharField(max_length=40, null=True, blank=True)  # 상세주소
    birth = models.DateTimeField(default=timezone.now)  # 나이
    nickname = models.CharField(null=True, unique=True, max_length=20)
    kakao_id = models.CharField(null=True, unique=True, max_length=100)
    followings = models.ManyToManyField("self", symmetrical=False, related_name="followers")
    blocking = models.ManyToManyField(
        "self", symmetrical=False, related_name="blockers"
    )

    image = ProcessedImageField(
        upload_to="image/",
        format="JPEG",
        processors = [
            Transpose(),
        ],
        options={"quality": 30},
        blank=True,
        null=True,
    )
    received_mail = models.IntegerField(default=0, null=True)

    STORTS_CHOICES = (
        ("축구", "축구"),
        ("농구", "농구"),
        ("야구", "야구"),
        ("클라이밍", "클라이밍"),
        ("등산", "등산"),
        ("테니스", "테니스"),
        ("트래킹", "트래킹"),
        ("볼링", "볼링"),
        ("러닝", "러닝"),
        ("스키", "스키"),
        ("보드", "보드"),
        ("헬스", "헬스"),
        ("산책", "산책"),
        ("플로깅", "플로깅"),
        ("자전거", "자전거"),
        ("서핑", "서핑"),
        ("배드민턴", "배드민턴"),
        ("탁구", "탁구"),
        ("골프", "골프"),
        ("스포츠경기", "스포츠경기"),
    )

    sports = MultiSelectField(  # 관심 운동 선택
        max_length=100,
        choices=STORTS_CHOICES,
        blank=True,
    )

    Travel_CHOICES = (
        ("복합문화공간", "복합문화공간"),
        ("테마파크", "테마파크"),
        ("피크닉", "피크닉"),
        ("드라이브", "드라이브"),
        ("캠핑", "캠핑"),
        ("국내여행", "국내여행"),
        ("해외여행", "해외여행"),
    )

    travel = MultiSelectField(  # 관심 여행 나들이 선택
        max_length=100,
        choices=Travel_CHOICES,
        blank=True,
    )

    ART_CHOICES = (
        ("전시", "전시"),
        ("영화", "영화"),
        ("뮤지컬", "뮤지컬"),
        ("공연", "공연"),
        ("디자인", "디자인"),
        ("박물관", "박물관"),
        ("연극", "연극"),
        ("콘서트", "콘서트"),
        ("연주회", "연주회"),
        ("페스티벌", "페스티벌"),
    )

    art = MultiSelectField(  # 관심 문화*예술 선택
        max_length=100,
        choices=ART_CHOICES,
        blank=True,
    )

    FOOD_CHOICES = (
        ("맛집투어", "맛집투어"),
        ("카페", "카페"),
        ("와인", "와인"),
        ("커피", "커피"),
        ("디저트", "디저트"),
        ("맥주", "맥주"),
        ("티룸", "티룸"),
        ("비건", "비건"),
        ("파인다이닝", "파인다이닝"),
        ("요리", "요리"),
        ("페어링", "페어링"),
        ("칵테일", "칵테일"),
        ("위스키", "위스키"),
        ("전통주", "전통주"),
    )

    food = MultiSelectField(  # 관심 음식 선택
        max_length=100,
        choices=FOOD_CHOICES,
        blank=True,
    )

    DEVELOP_CHOICES = (
        ("습관만들기", "습관만들기"),
        ("챌린지", "챌린지"),
        ("독서", "독서"),
        ("스터디", "스터디"),
        ("외국어", "외국어"),
        ("재테크", "재테크"),
        ("브랜딩", "브랜딩"),
        ("커리어", "커리어"),
        ("사이드프로젝트", "사이드프로젝트"),
    )

    develop = MultiSelectField(max_length=100, choices=DEVELOP_CHOICES, blank=True)  # 관심 음식 선택

    @property
    def get_photo_url(self):

        if self.profile_pic:
            return self.profile_pic.url
        return None
