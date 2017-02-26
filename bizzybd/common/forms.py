from django import forms
from django.forms import Form
from common.models import Website


class WebsiteForm(Form):
    name = forms.CharField(max_length=20, required=False)

    def clean(self):
        super(WebsiteForm, self).clean()
        website = self.cleaned_data.get('name')
        if(Website.objects.filter(name=website)):
            raise forms.ValidationError(
                "This name has already been taken choose another name")

    def save(self, user):
        name = self.cleaned_data.get('name')
        Website.objects.create(name=name, owner=user)


class DivForm(Form):
    id = forms.IntegerField(widget=forms.HiddenInput())
    name = forms.CharField()

    # def __init__(self, *args, **kwargs):
    #     super(DivForm, self).__init__(*args, **kwargs)

    #     if self.initial:
    #         div = self.initial
    #         print("\n\n going to print div")
    #         print(div)
            # self.fields['name'].initial = 'This is default text.'
            # self.name = "alamindiv"
