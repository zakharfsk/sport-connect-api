from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('swagger-ui', permanent=True)),
    path('api/v1/', include([
        path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
        path('', include('users.api.urls', namespace='authorization')),
    ])),
    path('calculations/', include('core.urls', namespace='core')),
    path("schema/", SpectacularAPIView.as_view(), name="schema")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
