# import datetime
from django.views import View


from django.http import HttpResponse
# from django.http import HttpResponseRedirect
# from django.shortcuts import redirect
import json as simplejson
from cards.models import Cards


def return_json(data):
    if(data):
        status = "Not Available"
    else:
        status = "Available"
    status = {'status': status}
    json = simplejson.dumps(status)
    return HttpResponse(json, content_type='application/javascript')


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
