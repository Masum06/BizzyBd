from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from common.views import login


urlpatterns = [
    # Examples:
    # url(r'^$', 'bizzybd.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^common/', include('common.urls')),
    url(r'^ajax_request/', include('ajax_request.urls')),
    url(r'^', include('home.urls', namespace='home')),
    url(r'^cards/', include('cards.urls', namespace='cards')),
    # for python social auth
    url('', include('social.apps.django_app.urls', namespace='social')),
    # for django default authentication system
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^accounts/login/$', login, name='login'),
    # url(r'^captcha/', include('captcha.urls')),
    # url(r'^ajax_select/', include(ajax_select_urls)),

]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
