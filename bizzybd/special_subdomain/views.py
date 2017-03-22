from django.shortcuts import render, redirect, HttpResponse
from django.views import View
# from django.shortcuts import get_object_or_404

class TeacherDemoView(View):

    # template_name = 'home/index.html'
    template_name = 'home/sub_domain.html'

    def get(self, request, *args, **kwargs):

        print("\n\n............In teacher demo view")

        return HttpResponse("Hello alamin")