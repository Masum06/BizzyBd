from django.db import models
# from django.db.models import Sum
# from django.contrib.auth.models import User
# from django.contrib.postgres.fields import ArrayField
# from ckeditor_uploader.fields import RichTextUploadingField
# from django.db.models.aggregates import Avg
# from gre_model_test.constants import DIFFICUTY_CHOICES, \
#     GRE_MCQ_TYPE_CHOICES, SECTION_TYPE_CHOICES

STATUS_CHOICES = (
    ('accepted', 'Accepted'),
    ('rejected', 'Rejected'),
    ('pending', 'Pending'),
)


class Themes(models.Model):

    name = models.CharField(max_length=50)
    theme_image = models.ImageField(blank=True, null=True)
    div1 = models.TextField(blank=True, null=True)
    div2 = models.TextField(blank=True, null=True)
    div3 = models.TextField(blank=True, null=True)
    div4 = models.TextField(blank=True, null=True)
    div5 = models.TextField(blank=True, null=True)
    div6 = models.CharField(max_length=300, blank=True, null=True)
    div7 = models.CharField(max_length=300, blank=True, null=True)
    div8 = models.CharField(max_length=300, blank=True, null=True)
    div9 = models.CharField(max_length=300, blank=True, null=True)
    div10 = models.CharField(max_length=300, blank=True, null=True)

    image1 = models.ImageField(blank=True, null=True)
    image2 = models.ImageField(blank=True, null=True)
    image3 = models.ImageField(blank=True, null=True)

    is_theme = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Cards(Themes):

    url = models.CharField(max_length=50, unique=True)
    status = models.CharField(choices=STATUS_CHOICES,
                              max_length=20,
                              help_text='Select Status of the Card: ',
                              default='pending')

    def __str__(self):
        return self.url
