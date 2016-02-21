from django.shortcuts import render
from django.views import generic
from . import models


class FilmDetailView(generic.DetailView):
    model = models.Film
    context_object_name = 'film'

    slug_url_kwarg = 'title'
    slug_field = 'title'


class FilmCreateView(generic.CreateView):
    model = models.Film
    fields = ['title', 'synopsis', 'released_date']


class FilmReviewDetailView(generic.DetailView):
    model = models.FilmReview
    context_object_name = 'film_review'


class FilmReviewCreateView(generic.CreateView):
    model = models.FilmReview
    fields = ['liked', 'content']

