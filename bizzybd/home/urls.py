from django.conf.urls import url
from home.views import IndexView, MysiteView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^mysite/$', MysiteView.as_view(), name='mysite'),

]
