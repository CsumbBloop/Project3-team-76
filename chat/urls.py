from django.conf.urls import url
from . import views
app_name = 'chat'
urlpatterns = [
    #/music/ 
    url(r'^$', views.IndexView.as_view(), name='index'),
    #/music/71/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(),name='detail'),
    #/music/71/favorite/
    url(r'^album/add/$', views.AlbumCreate.as_view(), name='album-add'),
    url(r'^album/add2/$', views.AlbumCreate2.as_view(), name='album-add2'),
    url(r'^album/add3/$', views.AlbumCreate3.as_view(), name='album-add3')
]
