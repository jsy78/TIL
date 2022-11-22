from django import forms
from froala_editor.widgets import FroalaEditor
from .models import Article, Review, Comment
from phonenumber_field.formfields import PhoneNumberField


class ArticleForm(forms.ModelForm):
    menu = forms.CharField(
        label="메뉴",
        widget=FroalaEditor(
            options={
                "toolbarSticky": False,
                "heightMin": 200,
            }
        ),
    )

    number = PhoneNumberField(
        label="전화번호",
        region="KR",
        required=False,
    )

    class Meta:
        model = Article
        fields = [
            "name",
            "address",
            "sido",
            "sigungu",
            "roadname",
            "number",
            "opening_hour",
            "menu",
            "parking",
            "dayoff",
            "cafeType",
            "image1",
            "image2",
            "image3",
        ]
        labels = {
            "name": "가게 이름",
            "address": "주소",
            "sido": "시/도",
            "sigungu": "시/군/구",
            "roadname": "도로명",
            "number": "전화번호",
            "opening_hour": "영업 시간",
            "menu": "메뉴",
            "parking": "주차",
            "dayoff": "휴일",
            "cafeType": "분류",
            "image1": "사진 1",
            "image2": "사진 2",
            "image3": "사진 3",
        }
        widgets = {
            "address": forms.TextInput(
                attrs={
                    "readonly": "True",
                }
            ),
            "sido": forms.HiddenInput(
                attrs={
                    "readonly": "True",
                }
            ),
            "sigungu": forms.HiddenInput(
                attrs={
                    "readonly": "True",
                }
            ),
            "roadname": forms.HiddenInput(
                attrs={
                    "readonly": "True",
                }
            ),
            "opening_hour": forms.TextInput(
                attrs={
                    "placeholder": "예) 오전 9시~오후 6시, 오후 8시~오전 2시",
                }
            ),
            "parking": forms.TextInput(
                attrs={
                    "placeholder": "예) 주차 공간 없음 / 무료 주차 가능 / ○시간 내 무료 주차 가능 / 유료 주차 가능",
                }
            ),
            "dayoff": forms.TextInput(
                attrs={
                    "placeholder": "예) 없음 / 일요일 / 토요일~일요일 / 화요일, 금요일",
                }
            ),
        }


class ReviewForm(forms.ModelForm):
    content = forms.CharField(
        label="내용",
        widget=FroalaEditor(
            options={
                "toolbarSticky": False,
                "heightMin": 300,
            }
        ),
    )

    class Meta:
        model = Review
        fields = [
            # "title",
            "rate",
            "content",
        ]
        labels = {
            # "title": "제목",
            "rate": "별점",
            "content": "내용",
        }
        widgets = {
            "rate": forms.NumberInput(
                attrs={
                    "step": "0.5",
                    "max": "5.0",
                    "min": "0.5",
                }
            ),
        }


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "댓글을 남겨보세요 💬",
            }
        ),
    )

    class Meta:
        model = Comment
        fields = [
            "content",
        ]


class ReplyForm(forms.ModelForm):
    content = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "대댓글을 남겨보세요 💬",
            }
        ),
    )

    class Meta:
        model = Comment
        fields = [
            "content",
        ]
