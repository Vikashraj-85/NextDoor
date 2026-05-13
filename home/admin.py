from django.contrib import admin
from django.contrib import admin
from .models import *

# Register your models here.
class PropertyImageAdmin(admin.TabularInline):
    
    model = PropertyImage

    extra = 3


class PropertyAdmin(admin.ModelAdmin):

    inlines = [PropertyImageAdmin]


admin.site.register(Property, PropertyAdmin)
admin.site.register(Profile)
admin.site.register(PropertyImage)
admin.site.register(Inquiry)
admin.site.register(Review)