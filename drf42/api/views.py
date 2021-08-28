from .models import Singer, Song
from .serializers import SingerSerializer, SongSerializer
from rest_framework import viewsets

class SingerViewSet(viewsets.ModelViewSet):
   queryset = Singer.objects.all()
   serializer_class = SingerSerializer

class SongViewSet(viewsets.ModelViewSet):
   queryset = Song.objects.all()
   serializer_class = SongSerializer   
   