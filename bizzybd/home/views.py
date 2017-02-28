from django.views import View
# from django.views.generic import TemplateView
from django.conf import settings
from django.shortcuts import render, redirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.forms.models import formset_factory

from common.models import Website, Div
from common.forms import WebsiteForm, DivForm


class IndexView(View):

    template_name = 'home/index.html'
    # template_sub_domain = 'home/sub_domain.html'

    def get(self, request, *args, **kwargs):

        print("IP Address for debug-toolbar: " + request.META['REMOTE_ADDR'])
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

            new_website_url = "http://" + form.cleaned_data['name'] + settings.DOMAIN_NAME + ':8000'
            print(new_website_url)
            return redirect(new_website_url)
            # return HttpResponseRedirect(new_website_url)

        else:

            context = {
                # 'mywebsites': mywebsites,
                'form': form,
            }
            return render(request, self.template_name, context)

        return HttpResponse("Website is created")


class EditorView(View):

    template_name = 'common/editor.html'
    DivFormSet = formset_factory(form=DivForm, extra=0)

    def get(self, request, *args, **kwargs):
        divs = Div.objects.all().values()
        formset = self.DivFormSet(initial=divs)
        form = DivForm(initial={'name': "alamin"})
        context = {
            'divs': divs,
            'formset': formset,
            'form': form,
        }
        # print(formset)
        return render(request, self.template_name, context)


class SlimView(View):

    template_name = 'common/slim.html'

    def get(self, request, *args, **kwargs):
        div = Div.objects.filter(name="ImageTest").first()
        context = {
            'div': div,
        }
        # print(formset)
        return render(request, self.template_name, context)



def get_subdomain_name(request):
    title = request.get_host()
    position = title.find(settings.DOMAIN_NAME)
    # print(title)
    # print(position)
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
