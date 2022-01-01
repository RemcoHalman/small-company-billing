from django.contrib import admin
from django.urls import path
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
]


admin.site.site_header = settings.ADMIN_SITE_HEADER
admin.site.site_title = settings.ADMIN_SITE_TITLE
admin.site.index_title = settings.ADMIN_INDEX_TITLE
admin.site.site_url = settings.ADMIN_SITE_URL
