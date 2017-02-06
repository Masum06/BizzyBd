from django.conf.urls import url
from subdomain.views import IndexView

urlpatterns = [
    url(r'^', IndexView.as_view(), name='index'),
    # url(r'^mysite/$', MysiteView.as_view(), name='mysite'),

]
