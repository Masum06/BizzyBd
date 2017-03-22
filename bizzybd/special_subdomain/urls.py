from django.conf.urls import url
from special_subdomain import views

urlpatterns = [
    url(r'^', views.TeacherDemoView.as_view(), name='teacher_demo'),
]
