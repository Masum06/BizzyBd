from django.db import models
from django.contrib.auth.models import User

CKEDITOR_DIV = "<div id='{0}' contenteditable='true'>\
                    {1}\
                </div>"


class Theme(models.Model):

    name = models.CharField(max_length=50, unique=True)
    # owner = models.ForeignKey(User)

    def __str__(self):
        return self.name


class Website(models.Model):

    name = models.CharField(max_length=50, unique=True)
    owner = models.ForeignKey(User)
    theme = models.ForeignKey(Theme)

    def __str__(self):
        return self.name


class Page(models.Model):

    name = models.CharField(max_length=50, unique=True)
    website = models.ForeignKey(Website, blank=True, null=True)
    theme = models.ForeignKey(Theme, blank=True, null=True)
    sequence_no = models.PositiveSmallIntegerField(default=1000)
    content = models.TextField(blank=True, null=True)
    div_format = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_full_page(self):
        if self.content:
            # s = s.format("div_id", "id", "bbbbbbbbbbbbbb")
            divs = Div.objects.filter(page=self).order_by("sequence_no")

            arguments = []
            arguments.append(self.name)
            all_div = ""
            for div in divs:
                if self.div_format:
                    div_str = self.div_format.format("div" + str(div.id), div.name)
                else:
                    div_str = CKEDITOR_DIV.format("div" + str(div.id), div.name)
                all_div += div_str
            arguments.append(all_div)
            # arguments = ["Resume", "alamin"]
            # print(arguments)
            # print(self.content)
            content = self.content.format(*arguments)
            return content
        return None


class Div(models.Model):

    website = models.ForeignKey(Website, blank=True, null=True)
    theme = models.ForeignKey(Theme, blank=True, null=True)
    page = models.ForeignKey(Page, blank=True, null=True)
    sequence_no = models.PositiveSmallIntegerField(default=1000)
    name = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="slim/", blank=True, null=True)
    file = models.FileField(upload_to='filepicker/', blank=True, null=True)

    def __str__(self):

        return self.get_name()

    def get_name(self):

        if self.name:
            return self.name[0:70]
        else:
            return 'Div'
