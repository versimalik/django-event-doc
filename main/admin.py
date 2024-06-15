from django.contrib import admin
from .models import Event, EventPhoto
from django.utils.safestring import mark_safe

# Register your models here.

class EventPhotoAdmin(admin.ModelAdmin):

    def image(self, obj):
        return mark_safe(f"<img width='60' src='{obj.photo.url}'>");

    list_display=[
        'event',
        'image',
    ]

class EventPhotoInline(admin.StackedInline):
    model = EventPhoto

class EventAdmin(admin.ModelAdmin):

    inlines = [
        EventPhotoInline,
    ]

    list_display=[
        'title',
        'description',
        'date_start',
        'date_end',
        'created_at',
        'created_by'
    ]

    exclude=[
        'created_by',
    ]

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Event, EventAdmin)
admin.site.register(EventPhoto, EventPhotoAdmin)