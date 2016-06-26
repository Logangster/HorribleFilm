from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view()),
    url(r'^account/', include('django.contrib.auth.urls')),
    url(r'^account/', include('registration.backends.hmac.urls')),
    url(r'^user/', include('users.urls')),
    url(r'^film/', include('films.urls')),
    url(r'^admin/', admin.site.urls),
]
