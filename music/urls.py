from django.urls import path
from . import views  #. means the sme dir

#specify to which app does this url file is asociated with
app_name='music'

urlpatterns = [
    path('',views.index,name='index'),
    #music/71/
    path('<album_id>/',views.detail, name='detail'),
    #sometimes the url does not  only directs you
    #to a differtent page, rather it preforms some
    #task and then take you to the different page.
                 #for example
    #the logout system:if you click logout,
    #it first,logs you out
    #then, directs you to a page(homepage)

    #music/71/favourite
    path('<album_id>/favourite/',views.favourite, name='favourite'),

]
