from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    grade = forms.FloatField(
        required=True,
        max_value=5,
        min_value=0.5,
        widget=forms.NumberInput(attrs={"step": "0.5"}),
    )

    class Meta:
        model = Review
        fields = "__all__"
