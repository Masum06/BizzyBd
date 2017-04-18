# import datetime
from django.views import View


from django.http import HttpResponse
# from django.http import HttpResponseRedirect
# from django.shortcuts import redirect
import json as simplejson
from cards.models import Cards
from common.models import Div
from common.forms import DivForm

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class UrlCheckView(View):

    def get(self, request, *args, **kwargs):
        url = request.GET.get('url')
        # json = {'data': ''}
        data = ""
        if(url):
            data = Cards.objects.filter(url=url)

        return return_json(data)

    def post(self, request, *args, **kwargs):
        pass


class UpdateDiv(View):

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
        text = request.POST.get('text')
        form = DivForm(request.POST)
        if(div_id):
            div = Div.objects.get(id=div_id)
            div.name = text
            div.save()
        else:
            print("\n\n ajax request with wrong div_id")
            print(div_id)
            print(text)
            print(form)

        status = {'status': True}
        json = simplejson.dumps(status)
        return HttpResponse(json, content_type='application/javascript')


class SlimAync(View):

    # @method_decorator(csrf_exempt)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(SlimAync, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        print("\n\n In get method")

        status = {'status': True}
        json = simplejson.dumps(status)
        return HttpResponse(json, content_type='application/javascript')

    def post(self, request, *args, **kwargs):

        print("ajax request post")
        # print(request.POST)
        print("\nFILES ARE BELOW")
        print(request.FILES)
        file = request.POST.get('slim[]')
        myfile = request.FILES.get('slim_output_4')
        if (not file or not myfile):
            # file = request.POST.get('file');
            # myfile = request.FILES.get('file')
            files = request.FILES
            # print(type(files))

            for f in files:
                # print(type(f))
                # print(f)
                # print(type(files[f]))
                Div.objects.create(name='FileUploadTesting', file=files[f])

                print("File upload complete")

        else:
            div = Div.objects.filter(name="ImageTest").first()
            print(div)
            if not div:
                Div.objects.create(name="ImageTest")
            div.image = myfile
            div.save()

        status = {'status': True}
        json = simplejson.dumps(status)
        return HttpResponse(json, content_type='application/javascript')


def return_json(data):
    if(data):
        status = "Not Available"
    else:
        status = "Available"
    status = {'status': status}
    json = simplejson.dumps(status)
    return HttpResponse(json, content_type='application/javascript')
