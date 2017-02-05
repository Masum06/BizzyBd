from django.views import View
# from django.views.generic import TemplateView
from django.conf import settings
from django.shortcuts import render, redirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

from common.models import Website
from common.forms import WebsiteForm



class IndexView(View):

    template_name = 'home/index.html'
    template_sub_domain = 'home/sub_domain.html'

    def get(self, request, *args, **kwargs):
        sub_domain_name = get_subdomain_name(request)
        if sub_domain_name:
            website = get_object_or_404(Website, name=sub_domain_name)
            context = {
                'website': website,
                'is_owner': is_owner(website, request),
            }
            return render(request, self.template_sub_domain, context)
        print("\n....not a subdomain name")

        context = {
            'title': "Bizzybd",
        }
        return render(request, self.template_name, context)


class MysiteView(View):

    template_name = 'home/mysite.html'
    form = WebsiteForm

    @method_decorator(login_required(login_url=reverse_lazy('home:index')))
    def get(self, request, *args, **kwargs):
        mywebsites = None
        if(request.user.is_authenticated()):
            mywebsites = Website.objects.filter(owner=request.user)
        context = {
            'mywebsites': mywebsites,
            'form': self.form(),
        }

        return render(request, self.template_name, context)

    @method_decorator(login_required(login_url=reverse_lazy('home:index')))
    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)

        if(form.is_valid()):
            form.save(request.user)
            print("Website has been created")

        else:

            context = {
                # 'mywebsites': mywebsites,
                'form': form,
            }
            return render(request, self.template_name, context)

        return HttpResponse("Website is created")


def get_subdomain_name(request):
    title = request.get_host()
    position = title.find(settings.DOMAIN_NAME)
    print(title)
    print(position)
    if (position != -1):
        title = title[:position]
        return title
    else:
        return None


def is_owner(website, request):

    if(website.owner == request.user):
        return True
    else:
        return False
