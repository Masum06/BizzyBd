from django.conf.urls import include, url
from django.contrib import admin

from common.views import login


urlpatterns = [
    # Examples:
    # url(r'^$', 'bizzybd.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^common/', include('common.urls')),
    url(r'^', include('home.urls', namespace='home')),
    # for python social auth
    url('', include('social.apps.django_app.urls', namespace='social')),
    # for django default authentication system
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^accounts/login/$', login, name='login'),
]
