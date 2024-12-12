from django import forms
from . import models
class CreateReviewForm(forms.ModelForm):
    communication = forms.IntegerField(
        max_value=5,
        min_value=1,
        label="برخورد میزبان",
        widget=forms.NumberInput(attrs={"style": "text-align: right;"})
    )
    cleanliness = forms.IntegerField(
        max_value=5,
        min_value=1,
        label="نظافت",
        widget=forms.NumberInput(attrs={"style": "text-align: right;"})
    )
    location = forms.IntegerField(
        max_value=5,
        min_value=1,
        label="موقعیت مکانی",
        widget=forms.NumberInput(attrs={"style": "text-align: right;"})
    )
    value = forms.IntegerField(
        max_value=5,
        min_value=1,
        label="ارزش کلی",
        widget=forms.NumberInput(attrs={"style": "text-align: right;"})
    )

    class Meta:
        model = models.Review
        fields = (
            "review",
            "communication",
            "cleanliness",
            "location",
            "value",
        )
        labels = {
            "review": "نظر",
        }
        widgets = {
            "review": forms.Textarea(attrs={"style": "text-align: right;", "placeholder": "نظر خود را وارد کنید"})
        }

    def save(self):
        review = super().save(commit=False)
        return review
