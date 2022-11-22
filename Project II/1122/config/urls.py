from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("cafes/", include("cafes.urls")),
    path("froala_editor/", include("froala_editor.urls")),
]

if settings.DEBUG:
    import debug_toolbar, mimetypes

    mimetypes.add_type("application/javascript", ".js", True)

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
