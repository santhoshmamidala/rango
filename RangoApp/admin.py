from django.contrib import admin
from RangoApp.models import Category, Page, UserProfile

#This class can be used to customize the admin interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page)
admin.site.register(UserProfile)

