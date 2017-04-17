from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.utils.decorators import method_decorator

from lazysignup.decorators import allow_lazy_user
from django.shortcuts import get_object_or_404

from common.models import Website, Page, Div


class TeacherDemoView(View):

    template_name = 'special_subdomain/teacher/teacher.html'

    def get(self, request, *args, **kwargs):
        request.session.set_expiry(300)

        context = {
            'edit_mode': False,
        }
        print("session key")
        print(request.session.session_key)
        return render(request, self.template_name, context)


class TeacherDemoEditView(View):

    template_name = 'special_subdomain/teacher/teacher.html'

    @method_decorator(allow_lazy_user)
    def get(self, request, *args, **kwargs):
        website = get_object_or_404(Website, name='teacher')
        pages = Page.objects.filter(website=website).order_by('sequence_no')
        print(pages)
        context = {
            'edit_mode': True,
            'website': website,
            'pages': pages,
        }

        for p in pages:
            # print(p.content)
            print(p.get_full_page())
            # if p.content is not None:
            #     print("foor loop")
            #     s = p.content
            #     s = s.format("div_id", "id", "bbbbbbbbbbbbbb")
            #     print(s)
        # print("after loop")



        return render(request, self.template_name, context)


class TeacherDemoEditView2(View):

    template_name = 'special_subdomain/teacher/teacher2.html'

    @method_decorator(allow_lazy_user)
    def get(self, request, *args, **kwargs):
        website = get_object_or_404(Website, name='teacher')
        pages = Page.objects.filter(website=website)
        print(pages)
        context = {
            'edit_mode': True,
            'website': website,
            'pages': pages,
        }


        return render(request, self.template_name, context)
