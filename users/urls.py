from django.conf.urls import include
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'profile/edit/', views.ProfileUpdateView.as_view(), name='edit-profile'),
    url(r'(?P<username>[^/]+)/', views.ProfileDetailView.as_view(), name='user-profile'),
]