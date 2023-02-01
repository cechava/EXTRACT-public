from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TravelAgentProfile


@admin.register(TravelAgentProfile)
class TravelAgentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'keywords', 'profile', 'calendly_link')
    readonly_fields = ['img_preview']
