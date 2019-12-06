"""katz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


# Url for admin access
urlpatterns = [
    path('admin/', admin.site.urls),
]

from django.urls import include

# URL for static files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Url paths for teamapp, accounts and when no specific path is given
urlpatterns += [
    path('teamapp/', include('teamapp.urls')),
    path('', RedirectView.as_view(url='/teamapp/', permanent=True)),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf import settings
from django.conf.urls.static import static
