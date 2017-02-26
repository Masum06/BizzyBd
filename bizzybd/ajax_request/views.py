# import datetime
from django.views import View


from django.http import HttpResponse
# from django.http import HttpResponseRedirect
# from django.shortcuts import redirect
import json as simplejson
from cards.models import Cards
from common.models import Div
from common.forms import DivForm


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


def return_json(data):
    if(data):
        status = "Not Available"
    else:
        status = "Available"
    status = {'status': status}
    json = simplejson.dumps(status)
    return HttpResponse(json, content_type='application/javascript')
