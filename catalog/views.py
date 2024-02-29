from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Book, Video, Game
from django.shortcuts import render


def index(request):
    return render(request, 'catalog/index.html')

def ItemListView(request):
    books = Book.objects.all()
    videos = Video.objects.all()
    games = Game.objects.all()
    context = {
        'books': books,
        'videos': videos,
        'games': games
    }
    return render(request, 'catalog/item_list.html', context)


class BookListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'catalog/book_list.html'

class VideoListView(ListView):
    model = Video
    context_object_name = 'video_list'
    template_name = 'catalog/video_list.html'

class GameListView(ListView):
    model = Game
    context_object_name = 'game_list'
    template_name = 'catalog/game_list.html'

class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'catalog/book_detail.html'

class VideoDetailView(DetailView):
    model = Video
    context_object_name = 'video'
    template_name = 'catalog/video_detail.html'

class GameDetailView(DetailView):
    model = Game
    context_object_name = 'game'
    template_name = 'catalog/game_detail.html'

