from django.views import generic
from .models import Album23
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy


class IndexView(generic.ListView):
    template_name = 'chat/index.html'
    fields = ['album_title','album_logo']
    model = Album23

    def get_queryset(self):
        return Album23.objects.all()


class DetailView(generic.DetailView):
    model = Album23
    template_name = 'chat/detail.html'


class AlbumCreate(CreateView):
    model = Album23
    template_name = 'chat/album_form.html'

    def get_queryset(self):
        return Album23.objects.all()
    fields = ['album_title']
class AlbumCreate2(CreateView):
    model = Album23
    template_name = 'chat/album_form2.html'

    def get_queryset(self):
        return Album23.objects.all()
    fields = ['album_logo']
class AlbumCreate3(CreateView):
    model = Album23
    template_name = 'chat/album_form3.html'

    def get_queryset(self):
        return Album23.objects.all()
    fields = ['album_logo2']


