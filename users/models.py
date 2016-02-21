from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    about_me = models.TextField(default='')

    def __unicode__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('user-profile', kwargs={
            'username': self.user.username,
        })


class UserProfileTagType(models.Model):
    name = models.CharField(max_length=16, unique=True)


class UserProfileTagValue(models.Model):
    value = models.TextField(unique=True)


class UserProfileTag(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    type = models.ForeignKey(UserProfileTagType)
    value = models.ForeignKey(UserProfileTagValue)


def create_user_profile(**kwargs):
    UserProfile.objects.get_or_create(user=kwargs['instance'])


post_save.connect(create_user_profile, sender=User)