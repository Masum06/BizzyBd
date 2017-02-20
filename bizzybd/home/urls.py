from django.conf.urls import url
from home import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^mysite/$', views.MysiteView.as_view(), name='mysite'),
    url(r'^editor/$', views.EditorView.as_view(), name='editor'),
]
