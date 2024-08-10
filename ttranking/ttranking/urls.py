from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler400, handler404, handler500
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('matches/', include('matches.urls')),
    path('players/', include('players.urls')),
    path('admin-panel/', include('admin_panel.urls')),  # Include the admin panel URLs
    path('', include('core.urls')),  # Include core app urls

    # api path
    path('api/', include('api.urls')),
]

# Custom error handlers
handler400 = 'core.views.bad_request'
handler404 = 'core.views.page_not_found'
handler500 = 'core.views.server_error'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
