from django.conf.urls import url
from django.contrib.auth import views as auth_views
from accounts import views


app_name = 'accounts'

urlpatterns = [

    url(r'^main', views.main_page_view, name='main_page'),
    url(r'^logout/$', auth_views.logout, name='logout'),

]