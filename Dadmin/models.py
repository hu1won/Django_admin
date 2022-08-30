from django.db import models
from django.utils.translation import ugettext_lazy as _
import django.contrib.auth as auth
# Create your models here.

class User(models.Model):
    user = models.OneToOneField(auth.models.User, default='', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100, null=False, default='', help_text=_('name'))
    birth = models.DateField(max_length=100, null=False, default='', help_text=_('date_of_birth'))
    height = models.IntegerField(null=False, default=0, help_text=_('height_unit'))
    weight = models.IntegerField(null=False, default=0, help_text=_('weight_unit'))
    sex  = models.BooleanField(default=False, help_text=_('gender_text'))
    profile_img = models.CharField(max_length=255, null=False, default='', help_text=_('profile_img'))
    language = models.CharField(max_length=255, null=False, default='ko-KR', help_text=_('language'))
    point = models.IntegerField(null=False, default=0, help_text=_('point'))
    combine_point = models.IntegerField(null=False, default=0, help_text=_('combine_point'))
    access_level = models.BooleanField(default=True, help_text=_('access_level'))
    create_dttm = models.DateTimeField(auto_now=False, auto_now_add=True, help_text=_('create_dttm'))
        
    def __str__(self):
        return f'{self.nickname} | {self.birth} | {self.height} | {self.weight}'