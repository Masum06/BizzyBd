from django.views import View
# from django.views.generic import TemplateView
from django.shortcuts import render, redirect


class IndexView(View):

    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        title = request.get_host()
        position = title.find('.bizzybd')
        if (position != -1):
            title = title[:position]
        pos = title.find(':8000')
        if(pos != -1):
            title = title[:pos]
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
