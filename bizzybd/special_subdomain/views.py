from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.utils.decorators import method_decorator

from lazysignup.decorators import allow_lazy_user
# from django.shortcuts import get_object_or_404


class TeacherDemoView(View):

    template_name = 'special_subdomain/teacher.html'

    def get(self, request, *args, **kwargs):
        request.session.set_expiry(300)

        context = {
            'edit_mode': False,
        }
        print("session key")
        print(request.session.session_key)
        return render(request, self.template_name, context)


class TeacherDemoEditView(View):

    template_name = 'special_subdomain/teacher.html'

    @method_decorator(allow_lazy_user)
    def get(self, request, *args, **kwargs):
        context = {
            'edit_mode': True,
        }
        print("session key")
        print(request.user.is_authenticated())
        print(request.session.session_key)
        return render(request, self.template_name, context)
