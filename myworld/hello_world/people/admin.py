from django.contrib import admin
from .models import People

# Register your models here.
#admin.site.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display  = ("firstname", "lastname", "age",)

admin.site.register(People, PeopleAdmin)