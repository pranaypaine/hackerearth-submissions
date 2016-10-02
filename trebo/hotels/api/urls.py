from django.conf.urls import url
from django.contrib import admin

"""
	url routing for the app posts
"""
from  .views import(
	HotelListAPIView,
	HotelSearchAPIView
)

urlpatterns = [
    url(r'^list/$', HotelListAPIView.as_view(), name="list"),
    url(r'^search/$', HotelSearchAPIView.as_view(), name="list"),
    #url(r'^create/$', post_create, name="add"),
    #url(r'^edit/(?P<id>\d+)/$', post_update, name="edit"),
    #url(r'^(?P<id>\d+)/$', post_detail, name="detail"),
    #url(r'^(?P<id>\d+)/delete/$', post_delete, name="delete"),
    #url(r'^login/$', login, name="login"),

]