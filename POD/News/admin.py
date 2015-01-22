from django.contrib import admin
from News.models import Event, Photo

class CollectionAdmin(admin.ModelAdmin):
 
    class Media:
        js = (
            '/static/News/tinymce/tinymce.min.js',
        )
 
admin.site.register(Event, CollectionAdmin)
admin.site.register(Photo)


# Register your models here.
