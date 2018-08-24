from django.contrib import admin


# Register your models here.
from web.models import Product, Advisory


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'produce', 'capacity', 'degree')
    list_filter = ('title', 'author')


class AdvisoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'author')
    list_filter = ('title', 'author')


admin.site.register(Product, ProductAdmin)
admin.site.register(Advisory, AdvisoryAdmin)

admin.site.site_header = '龙驿酒庄后台管理系统'
admin.site.site_title = '龙驿酒庄'