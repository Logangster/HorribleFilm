from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models


class Film(models.Model):
    title = models.CharField(max_length=128)
    synopsis = models.TextField(default='')
    released_date = models.DateField()


class FilmReview(models.Model):
    film = models.ForeignKey(Film)
    liked = models.BooleanField()
    content = models.TextField()

    def get_absolute_url(self):

        return reverse('review-detail', kwargs={
            'review_id': self.pk,
        })
