from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

from sport_connect_api.docs_settings import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('schema-swagger-ui', permanent=True)),
    path('api/v1/', include([
        path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('', include('users.api.urls', namespace='authorization')),
        path('results/', include('core.api.urls', namespace='core_api'))
    ])),
    path('calculations/', include('core.urls', namespace='core')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
