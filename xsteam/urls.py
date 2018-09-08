"""xsteam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.decorators.csrf import ensure_csrf_cookie
import vendors.views


urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', ensure_csrf_cookie(TemplateView.as_view(template_name=''))),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^auth_api/', include('auth_api.urls')),
    url(r'^token/', include('tokens.urls')),
    url(r'^vendor/', include('vendors.urls')),
    url(r'^category/', include('categories.urls')),
    url(r'^course/', include('courses.urls')),
    url(r'^customer/', include('customers.urls')),
    url(r'^register/', vendors.views.register, name="注册"),
    url(r'^login/', vendors.views.login, name="登录"),
    url(r'^logout/', vendors.views.logout, name="登出"),
    url(r'^home/', vendors.views.home, name="主页"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
