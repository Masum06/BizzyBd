from django.conf.urls import url
from django.views.generic import TemplateView

from special_subdomain import views

urlpatterns = [
    url(r'^$', views.TeacherDemoView.as_view(), name='teacher_demo'),
    url(r'^edit/$', views.TeacherDemoEditView.as_view(), name='teacher_demo-edit'),
    url(r'^CSE313/$', TemplateView.as_view(template_name='special_subdomain/teacher/CSE313.html'),
        name='special_subdomain_CSE313'),
    url(r'^CSE313/evaluation/$', TemplateView.as_view(
        template_name='special_subdomain/teacher/CSE313_evaluation.html'),
        name='special_subdomain_CSE313_evaluation'),
    url(r'^ajax/div/$', views.AjaxUpdateDiv.as_view(), name='ajax_div'),
    url(r'^original/edit/$', views.TeacherDemoEditView2.as_view(), name='teacher_demo-edit'),
]
