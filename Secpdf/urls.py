"""
URL configuration for Secpdf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from Secpdf import views
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings
from django.conf.urls import handler404
from django.conf.urls import handler500

# Set the custom handler
handler404 = 'Secpdf.views.custom_page_not_found_view'
handler500 = 'Secpdf.views.custom_server_error_view'

# URL patterns for the application
urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('', views.homePage,name='Home'),
    path('encrypt/', views.encrypt,name='encrypt'),
    path('encrypt_file/', views.encrypt_file,name='encrypt_file'),
    path('decrypt/', views.decrypt,name='decrypt'),
    path('decrypt_file/', views.decrypt_file,name='decrypt_file'),
    path('response/', views.response,name='response'),
   ]
