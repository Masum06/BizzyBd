from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.shortcuts import get_object_or_404

from common.models import Website


class IndexView(View):

    # template_name = 'home/index.html'
    template_name = 'home/sub_domain.html'

    def get(self, request, *args, **kwargs):


        website = get_object_or_404(Website, name=request.subdomain)
        context = {
            'website': website,
            'is_owner': is_owner(website, request),
        }
        return render(request, self.template_name, context)



def is_owner(website, request):

    if(website.owner == request.user):
        return True
    else:
        return False
