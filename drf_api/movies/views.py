from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .serializer import MovieSerializer
from .models import Movie

# Create your views here.
class MoviesListView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailsView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer