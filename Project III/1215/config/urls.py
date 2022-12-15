"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("hobby/", include("hobby.urls")),
    path("community/", include("community.urls")),
    path("chat/", include("chat.urls")),
    # 소셜
    path("products/", include("products.urls")),
    path("summernote/", include("django_summernote.urls")),
    path("notes/", include("notes.urls")),

]

if settings.DEBUG:
    import debug_toolbar, mimetypes

    mimetypes.add_type("application/javascript", ".js", True)

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
