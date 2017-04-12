from django.conf.urls import url
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^index/$', views.index, name='index'),
    url(r'^login/$', views.UserLoginView.as_view(), name='login'),
    #url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout_user'),
    #url(r'^login_user/$', views.login_user, name='login_user'),
    #url(r'^register/$', views.UserFormView.as_view(), name="register"),
    url(r'^register/$', views.register, name="register"),
    #url(r'^(?P<profile_id>[0-9]+)/$', views.profile, name='profile'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^settings/$', views.settings, name='settings')
]   +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
