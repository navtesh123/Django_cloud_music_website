#    try:
#        album=Album.objects.get(pk=album_id)
#    except Album.DoesNotExist:
#        raise Http404("album does not exist")
#    return render(request,'music/detail.html',{'album':album})

#***all of the above code can be shortned by importing get_objects_or_404
#***from django.shortcuts

from django.shortcuts import render, get_object_or_404
from .models import Album, Song


def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', {'all_albums': all_albums})


def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})


def favourite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
         return render(request, 'music/detail.html', {
             'album': album,
             'error_message': "No song selected",
        })

    else:
        selected_song.is_favourite = True
        selected_song.save()
    return render(request, 'music/detail.html', {'album': album})
