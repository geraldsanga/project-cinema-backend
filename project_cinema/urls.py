from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = 'Project Cinema Admin'
admin.site.site_title = 'Project Cinema'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('core.api.urls')),
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
