from django.urls import path
from . import views

#specify to which app does this url file is asociated with
app_name='music'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    #music/71/
    path('<pk>/',views.DetailView.as_view(),name='detail'),
    #music/album/add/
    path('album/add/',views.AlbumCreate.as_view(),name='album-add'),
    ]
