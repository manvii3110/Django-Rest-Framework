from rest_framework import serializers
from .models import Singer, Song

class SongSerializer(serializers.ModelSerializer):    
    class Meta:
        model= Song
        fields=['id', 'title', 'singer', 'duration']       

class SingerSerializer(serializers.ModelSerializer):  
    song = serializers.HyperlinkedIdentityField(view_name='song-detail')  
    class Meta:
        model= Singer
        fields=['id', 'name', 'gender', 'song']

 