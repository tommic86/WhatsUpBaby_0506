"""whatsupbaby URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', 'accounts.views.login'),
    url(r'^accounts/auth/$', 'accounts.views.auth_view'),
    url(r'^accounts/logout/$', 'accounts.views.logout'),
    url(r'^accounts/loggedin/$', 'accounts.views.loggedin'),
    url(r'^accounts/invalid/$', 'accounts.views.invalid_login'),
    url(r'^rodzic/home/$', 'rodzic.views.home'),
    url(r'^dziecko/(?P<pk>\d+)/$', 'rodzic.views.dziecko_szczegoly', name='dziecko_szczegoly'),
    url(r'^opiekun/loggedin/$', 'opiekun.views.loggedin'),
    url(r'^opiekun/lista_dzieci/$', 'opiekun.views.lista_dzieci'),
    url(r'^opiekun/home/$', 'opiekun.views.home'),
    url(r'^tablica/$', 'tablica.views.posty', name='tablica'),
    url(r'^tablica/post_new/$', 'tablica.views.post_new', name='post_new'),
    url(r'^tablica/post/(?P<pk>[0-9]+)/$', 'tablica.views.post_detail', name='post_detail')
]
