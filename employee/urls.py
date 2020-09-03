from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include URLs from apps
    re_path('', include(r'apps.department.urls')),
    re_path('', include(r'apps.person.urls')),
    re_path('', include(r'apps.home.urls')),   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)