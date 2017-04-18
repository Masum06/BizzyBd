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
        context = {
            'edit_mode': True,
            'website': website,
            'pages': pages,
            'full_pages': full_pages,
        }

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
