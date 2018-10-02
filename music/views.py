# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse, Http404
# from .models import Album, Song


# # Create your views here.
# def index(request):
#     all_album = Album.objects.all()
#     return render (request, 'music/index.html', {'all_album': all_album})

# def details(request, album_id):
#     album = get_object_or_404(Album, pk = album_id)

#     return render(request, 'music/details.html', {'album': album})

# def favorite(request, album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     try:
#         selected_song = album.song_set.get(pk = request.POST['song'])
#     except:
#         return render(request, 'music/details.html', {'album': album})
#     else:
#         selected_song.is_favorite = True
#         selected_song.save()
#         return render(request, 'music/details.html', {'album': album})


from django.views import generic
from .models import Album, Song

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_album'

    def get_queryset(self):
        return Album.objects.all()

class DetailsView(generic.DetailView):
    model = Album 
    template_name = 'music/details.html'