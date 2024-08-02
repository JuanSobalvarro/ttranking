from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler400, handler404, handler500
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('matches/', include('matches.urls')),
    path('players/', include('players.urls')),
    path('', include('core.urls')),  # Include core app urls
]

# Custom error handlers
handler400 = 'core.views.bad_request'
handler404 = 'core.views.page_not_found'
handler500 = 'core.views.server_error'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)