from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler400, handler404, handler500
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('api/', include('core.urls')),
    path('api/players/', include('players.urls')),
    path('api/matches/', include('matches.urls')),
    path('api/seasons/', include('seasons.urls')),
    path('api/admin/', include('admin_panel.urls'))
]

# Custom error handlers
handler400 = 'core.views.bad_request'
handler404 = 'core.views.page_not_found'
handler500 = 'core.views.server_error'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
