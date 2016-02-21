from django.shortcuts import render
from django.views import generic
from . import models


class ProfileDetailView(generic.DetailView):
    """ Displays details about a user profile. """
    model = models.UserProfile
    context_object_name = 'user_profile'

    slug_url_kwarg = 'username'
    slug_field = 'user__username'


class ProfileUpdateView(generic.UpdateView):
    model = models.UserProfile
    fields = ['about_me']

    def get_object(self, queryset=None):
        if not queryset:
           queryset = self.get_queryset()
        print(self.request.user)
        return queryset.get(user=self.request.user)