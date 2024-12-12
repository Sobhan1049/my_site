from django import forms
from django_countries.fields import CountryField
from iranian_cities.fields import ShahrField
from . import models


class SearchForm(forms.Form):

    city = ShahrField().formfield()
    country = forms.CharField()
    room_type = forms.ModelChoiceField(
        required=False, empty_label="Any kind", queryset=models.RoomType.objects.all()
    )
    price = forms.IntegerField(required=False)
    guests = forms.IntegerField(required=False)
    bedrooms = forms.IntegerField(required=False)
    beds = forms.IntegerField(required=False)
    bathrooms = forms.IntegerField(required=False)
    instant_book = forms.BooleanField(required=False)
    superhost = forms.BooleanField(required=False)
    amenities = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Amenity.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    facilities = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Facility.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

class CreatePhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ("caption", "file")
        labels = {"caption": "کپشن", "file": "فایل"}
        widgets = {"caption": forms.TextInput(attrs={"style": "text-align: right;"}),

                   }

    def save(self, pk, *args, **kwargs):
        photo = super().save(commit=False)
        room = models.Room.objects.get(pk=pk)
        photo.room = room
        photo.save()

class CreateRoomForm(forms.ModelForm):
    class Meta:
        model = models.Room
        fields = (
            "name",
            "description",
            "country",
            "city",
            "price",
            "address",
            "guests",
            "beds",
            "bedrooms",
            "bathrooms",
            "check_in",
            "check_out",
            "instant_book",
            "room_type",
            "amenities",
            "facilities",
            "house_rules",
        )
        labels = {
            "name": "نام" ,
            "description": "توضیحات",
            "country": "کشور",
            "city": "شهر",
            "price": "قیمت",
            "address": "آدرس",
            "guests": "تعداد مهمان",
            "beds": "تعداد تخت",
            "bedrooms": "تعداد اتاق خواب",
            "bathrooms": "تعداد حمام",
            "check_in": "زمان ورود",
            "check_out": "زمان خروج",
            "instant_book": "فوری",
            "room_type": "نوع اتاق",
            "amenities": "امکانات",
            "facilities": "خدمات",
            "house_rules": "قوانین خانه",
        }
        widgets = {
            "name": forms.TextInput(attrs={"style": "text-align: right;"}),
            "description": forms.Textarea(attrs={"style": "text-align: right;"}),
            "country": forms.TextInput(attrs={"style": "text-align: right;"}),
            "price": forms.NumberInput(attrs={"style": "text-align: right;"}),
            "address": forms.TextInput(attrs={"style": "text-align: right;"}),
            "guests": forms.NumberInput(attrs={"style": "text-align: right;"}),
            "beds": forms.NumberInput(attrs={"style": "text-align: right;"}),
            "bedrooms": forms.NumberInput(attrs={"style": "text-align: right;"}),
            "bathrooms": forms.NumberInput(attrs={"style": "text-align: right;"}),
            "check_in": forms.TimeInput(attrs={"style": "text-align: right;"}),
            "check_out": forms.TimeInput(attrs={"style": "text-align: right;"}),
            "instant_book": forms.CheckboxInput(attrs={"style": "text-align: right;"}),
            "room_type": forms.Select(attrs={"style": "text-align: right;"}),
        }

    def save(self, *args, **kwargs):
        room = super().save(commit=False)
        return room


