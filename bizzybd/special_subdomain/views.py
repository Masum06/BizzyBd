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
            # forking theme to the website. creating a new website with default theme data
            divs = Div.objects.filter(theme=theme, website=None)
            for div in divs:
                div.id = None
                div.save()
                div.website = website
                div.save()
            website.div1 = theme.div1
            website.div2 = theme.div2
            website.div3 = theme.div3
            website.div4 = theme.div4
            website.div5 = theme.div5
            website.div6 = theme.div6
            website.div7 = theme.div7
            website.div8 = theme.div8
            website.div9 = theme.div9
            website.div10 = theme.div10
            website.save()

            print("\n\n ******** created new website for this user ********\n\n")

        print("Theme and website div1")
        print(theme.div1)
        print(website.div1)
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

        # print(website.div1.image.url)

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


class AjaxUpdateSlim(View):

    # @method_decorator(csrf_exempt)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(SlimAync, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        print("\n\n In get method")

        status = {'status': True}
        json = simplejson.dumps(status)
        return HttpResponse(json, content_type='application/javascript')

    def post(self, request, *args, **kwargs):

        # print("ajax request post")
        # # print(request.POST)
        # print("\n\n\n\nFILES ARE BELOW")
        # print(request.FILES)
        # print(request.POST)
        # print("\n\n")
        slim_data = request.POST.get("slim[]")
        slim_data = simplejson.loads(slim_data)
        meta = slim_data['meta']
        field = slim_data['output']['field']
        # print(field)
        # print(meta)
        # print(type(meta))
        div_id = meta['div_id']
        file = request.FILES.get(field)

        if(div_id and file):
            div = Div.objects.get(id=div_id)
            if div:
                div.image = file
                div.save()


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
