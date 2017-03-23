from django.shortcuts import render, redirect, HttpResponse
from django.views import View
# from django.shortcuts import get_object_or_404


class TeacherDemoView(View):

    template_name = 'special_subdomain/teacher.html'

    def get(self, request, *args, **kwargs):

        context = {
            'edit_mode': False,
        }
        return render(request, self.template_name, context)


class TeacherDemoEditView(View):

    template_name = 'special_subdomain/teacher.html'

    def get(self, request, *args, **kwargs):
        context = {
            'edit_mode': True,
        }
        return render(request, self.template_name, context)
