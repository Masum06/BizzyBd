from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.shortcuts import get_object_or_404

from common.models import Website


class IndexView(View):

    # template_name = 'home/index.html'
    template_name = 'cards/index.html'

    def get(self, request, *args, **kwargs):
        print("in cards index view")
        # website = get_object_or_404(Website, name=request.subdomain)
        context = {
            # 'website': website,
            # 'is_owner': is_owner(website, request),
        }
        return render(request, self.template_name, context)


class ThemesView(View):
    template_name = 'cards/themes.html'

    def get(self, request, *args, **kwargs):
        print("\n\n in themes views")


        context = {

        }
        return render(request, self.template_name, context)