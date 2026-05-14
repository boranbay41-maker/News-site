
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = "NewsTalk — Панель управления"
admin.site.site_title = "NewsTalk Admin"
admin.site.index_title = "Добро пожаловать"


urlpatterns = [
    path('newstalk-secret-panel/', admin.site.urls),
    path('', include('news_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
