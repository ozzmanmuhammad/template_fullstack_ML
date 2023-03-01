from django.contrib import admin
from .models import animalIdentifier
from django.utils.html import format_html

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        if obj.picture:
            return format_html('<h4>{}</h4>'.format(obj.picture.url))

    image_tag.short_description = 'Picture'

    list_display = ["image_tag","predicted","classified" , "uploaded"]
    search_fields = ('image_tag',"classified",'uploaded')
    list_per_page = 20


admin.site.register(animalIdentifier, ImageAdmin)