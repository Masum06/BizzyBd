from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.shortcuts import get_object_or_404
from cards.models import Themes, Cards
from cards.forms import CardsForm
from django.urls import reverse


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

        themes = Themes.objects.filter(is_theme=True)
        context = {
            'themes': themes,
        }
        return render(request, self.template_name, context)


class CardCreateView(View):
    template_name = 'cards/create_card.html'
    form = CardsForm

    def get(self, request, *args, **kwargs):
        theme_id = self.kwargs.get('theme_id')
        theme = get_object_or_404(Themes, id=theme_id)

        form = self.form(instance=theme)

        context = {
            'theme': theme,
            'form': form,
            # 'themes': themes,
        }
        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        # theme_id = self.kwargs.get('theme_id')
        # theme = get_object_or_404(Themes, id=theme_id)

        form = self.form(request.POST)

        if(form.is_valid()):
            form.save()
            url = form.cleaned_data.get('url')
            return redirect(reverse('cards_card', args=[url]))

            # return HttpResponse("Form is valid")
        else:

            context = {
                # 'theme': theme,
                'form': form,
                # 'themes': themes,
            }
            return render(request, self.template_name, context)
            return HttpResponse("Invalid")

        context = {
            'theme': theme,
            'form': form,
            # 'themes': themes,
        }
        return render(request, self.template_name, context)



class AllCardView(View):
    template_name = 'cards/all_cards.html'

    def get(self, request, *args, **kwargs):

        print("in all cards method")

        # card_url = self.kwargs.get('card_url')
        cards = Cards.objects.all()
        context = {
            'cards': cards,
        }
        return render(request, self.template_name, context)


class CardView(View):
    template_name = 'cards/card.html'

    def get(self, request, *args, **kwargs):

        card_url = self.kwargs.get('card_url')
        card = get_object_or_404(Cards, url=card_url)
        context = {
            'card': card,
        }
        return render(request, self.template_name, context)