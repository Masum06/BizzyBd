from django import forms
from django.forms import ModelForm
from cards.models import Themes, Cards
from captcha.fields import CaptchaField


class CardsForm(ModelForm):
    # name = forms.CharField(max_length=20, required=False)
    captcha = CaptchaField()

    class Meta:
        model = Cards
        exclude = ['status', 'is_theme']

    # def clean(self):
    #     super(WebsiteForm, self).clean()
    #     website = self.cleaned_data.get('name')
    #     if(Website.objects.filter(name=website)):
    #         raise forms.ValidationError(
    #             "This name has already been taken choose another name")

    # def save(self, user):
    #     name = self.cleaned_data.get('name')
    #     Website.objects.create(name=name, owner=user)
