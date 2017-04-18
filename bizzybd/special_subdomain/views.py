import json as simplejson

from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.utils.decorators import method_decorator

from lazysignup.decorators import allow_lazy_user
from django.shortcuts import get_object_or_404

from common.models import Theme, Website, Page, Div


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
        theme = Theme.objects.get(name="Teacher")
        website = Website.objects.filter(owner=request.user, theme=theme).last()
        if not website:
            website = Website.objects.create(
                name=request.user.username, owner=request.user, theme=theme)
            divs = Div.objects.filter(theme=theme, website=None)
            for div in divs:
                div.id = None
                div.save()
                div.website = website
                div.save()
            print("\n\n ******** created new website for this user ********\n\n")
        pages = Page.objects.filter(theme=website.theme).order_by('sequence_no')
        print(pages)
        full_pages = []
        for page in pages:
            full_pages.append(page.get_full_page(website))
        div_count = Div.objects.filter(website=website).count()
        div_count_str = 'X' * div_count
        context = {
            'edit_mode': True,
            'website': website,
            'pages': pages,
            'full_pages': full_pages,
            'div_count_str': div_count_str,

        }

        return render(request, self.template_name, context)


class AjaxUpdateDiv(View):

    def get(self, request, *args, **kwargs):
        # print("\n\n In get method")
        div_id = request.GET.get('div_id')
        text = request.GET.get('text')
        if(div_id):
            div = Div.objects.get(id=div_id)
            div.name = text
            div.save()
        status = {'status': True}
        json = simplejson.dumps(status)
        return HttpResponse(json, content_type='application/javascript')

    def post(self, request, *args, **kwargs):

        print("ajax request post")

        div_id = request.POST.get('div_id')
        print(div_id)
        print(div_id)
        text = request.POST.get('text')
        # form = DivForm(request.POST)
        if(div_id):
            div = Div.objects.get(id=div_id)
            if div.website.owner == request.user:
                div.name = text
                div.save()
        else:
            print("\n\n ajax request with wrong div_id")
            print(div_id)
            print(text)
            # print(form)

        status = {'status': True}
        json = simplejson.dumps(status)
        return HttpResponse(json, content_type='application/javascript')


class TeacherDemoEditView2(View):

    template_name = 'special_subdomain/teacher/teacher2.html'

    @method_decorator(allow_lazy_user)
    def get(self, request, *args, **kwargs):
        # website = get_object_or_404(Website, name='teacher')
        # pages = Page.objects.filter(website=website)
        # print(pages)
        context = {
            'edit_mode': True,
            # 'website': website,
            # 'pages': pages,
        }

        return render(request, self.template_name, context)
