from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin


urlpatterns = [
    url(r'^account/', include('django.contrib.auth.urls')),
    url(r'^account/', include('registration.backends.hmac.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^admin/', admin.site.urls),
]
