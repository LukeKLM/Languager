"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.conf import settings
from django.contrib import admin
from django.urls import include
from django.urls import path

from main.views.dashboard_view import index
from main.views.login_view import CustomLoginView
from main.views.login_view import CustomLogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("dictionary/", include("main.apps.dictionary.urls")),
    path("", index, name="index"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
