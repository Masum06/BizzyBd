from django.views import View
# from django.views.generic import TemplateView
from django.shortcuts import render, redirect


class IndexView(View):

    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        title = request.get_host()
        context = {
            'title': title
        }
        return render(request, self.template_name, context)

    # def post(self, request, *args, **kwargs):
    #     form = self.form(request.POST)
    #     if(not form.is_valid()):
    #         print(form.errors)
    #         return HttpResponse (form.errors)
    #     return render(request, self.template_post)
