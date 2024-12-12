from django.contrib import admin
from django.utils.html import mark_safe
from iranian_cities.admin import IranianCitiesAdmin
from . import models

@admin.register(models.RoomType, models.Facility, models.Amenity,models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """Item Admin Definition """
    list_display = ('name', 'used_by')
    def used_by(self, obj):
        return obj.rooms.count()
    pass



class PhotoInline(admin.TabularInline):
    model = models.Photo

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    inlines = (PhotoInline,)
    fieldsets = (
        (
            "Basic Info",
            {"fields":("name","description", "country", "city","address","price","room_type")}
        ),
        (
            "Times",
            {"fields":("check_in","check_out", "instant_book")}

        ),
        (
            "Spaces",
            {"fields": ("guests", "beds", "bedrooms", "bathrooms")}
        ),
        (
            "More About The Space",
            {    "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules")}
        ),
        ("Last Details",{"fields": ("host",)})
    )

    list_display = ('name',"country", "city", "price", "guests", "beds", "bedrooms", "bathrooms", "check_in", "check_out", "instant_book", "count_amenities", "count_photos","total_rating")

    list_filter = ("instant_book", "host__superhost", "room_type", "amenities", "facilities", 'city', "house_rules",'country')

    filter_horizontal = ("amenities", "facilities", "house_rules")

    search_fields = ("city","^host__username")
    raw_id_fields = ("host",  )

    def count_amenities(self, obj):

        return obj.amenities.count()

    def count_photos(self, obj): 
        return obj.photos.count()

    count_photos.short_description = "Photo Count"
@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """"""
    list_display = ("__str__","get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width = "50px" src="{obj.file.url}" />')


    get_thumbnail.short_description = "thumbnail"

