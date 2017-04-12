from django.db import models
from django.contrib.auth.models import User,Permission
from django.core.urlresolvers import reverse



class Place(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100,default='')
    license_id = models.CharField(max_length=100,default='')
    geo_loc = models.CharField(max_length=100,default='')

    profile_pic = models.ImageField(default='*')

    info = models.CharField(max_length=150,default='*')
    address = models.CharField(max_length=100,default='*')
    tel_num = models.CharField(max_length=50,default='*')

    facebooklink = models.CharField(max_length=200,default='*')
    twitterlink = models.CharField(max_length=200,default='*')
    instagramlink = models.CharField(max_length=200,default='*')

    menu = models.ImageField(default='*')

    reg_date = models.DateField(auto_now=True)


    def __str__(self):
        return str(self.username) + '-' +  self.company_name + '**************Create Date: ' + str(self.reg_date)



