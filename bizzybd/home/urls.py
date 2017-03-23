from django.conf.urls import url
from home import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^mysite/$', views.MysiteView.as_view(), name='mysite'),
    url(r'^editor/$', views.EditorView.as_view(), name='editor'),
    url(r'^slim/$', views.SlimView.as_view(), name='slim'),
    url(r'^filepicker/$', views.FilepickerView.as_view(), name='filepicker'),
]
