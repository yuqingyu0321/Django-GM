
# TODO
from django.contrib import admin


class MyAdminSite(admin.AdminSite):
    site_header = '祖玛管理系统'
    site_title = ' '
    index_title = '祖玛管理系统'


admin.site.site_header = MyAdminSite.site_header
admin.site.site_title = MyAdminSite.site_title
admin.site.index_title = MyAdminSite.index_title