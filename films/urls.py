from django.conf.urls import include
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'(?P<title>[^/]+)/', views.FilmDetailView.as_view(), name='film-detail'),
    url(r'(?P<title>[^/]+)/reviews/create', views.FilmReviewCreateView.as_view(), name='film-detail'),
    url(r'(?P<review_id>[^/]+)/', views.FilmReviewDetailView.as_view(), name='film-detail'),
]