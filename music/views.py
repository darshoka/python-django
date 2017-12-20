from django.http import Http404
from .models import Album
from django.shortcuts import render, get_object_or_404
# from django.template import loader


def index(request):
    all_albums = Album.objects.all()
    # template = loader.get_template('music/index.html')
    return render(request, 'music/index.html', {'all_albums': all_albums})
    # return HttpResponse(template.render(context, request))


def detail(request, album_id):
    # return HttpResponse("<h2> Details for  Album id :  " + str(album_id) + "</h2>")
    # album = Album.objects.get(pk=album_id)
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})
