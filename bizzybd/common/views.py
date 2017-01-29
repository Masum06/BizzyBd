from django.shortcuts import render


def login(request):
    next_url = request.GET.get('next', '#')
    return render(request, 'common/login.html', {'next_url': next_url})