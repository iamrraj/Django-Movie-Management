from rest_framework import serializers
from rmovie.models import Moviee, Cast,Detai
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField
    )

class DetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = Detai
    fields = ('pk','name','Status','Language','Budget','Revenue','Production_Companies','Production_Country','adult')


class CastSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cast
    fields = ('pk' ,'name','cname','cmname','role','murl')


class MovieSerializer(serializers.ModelSerializer): 
  class Meta:
    model = Moviee
    fields = ('pk','name','mdate','rating','murl','movietime','mtype','director','description','maincast','body','ytube')












class DCastSerializer(serializers.ModelSerializer):
  comments = MovieSerializer(many=True, read_only=True)
  class Meta:
    model = Cast
    fields = ('pk' ,'name','cname','cmname','role','murl','comments')



class DDetailSerializer(serializers.ModelSerializer):
  # comm = MovieSerializer(many=True)
  class Meta(object):
    model = Detai
    fields = ('pk','name','Status','Language','Budget','Revenue','Production_Companies','Production_Country','adult')

  # def create(self, validated_data):
  #       tracks_data = validated_data.pop('comm')
  #       album = Detai.objects.create(**validated_data)
  #       for track_data in tracks_data:
  #           Moviee.objects.create(album=album, **track_data)
  #       return album


class MovieDetailsSerializer(serializers.ModelSerializer):
  comments = CastSerializer(many=True)
  class Meta(object):
    model = Moviee
    fields = ('name','mdate','rating','murl','movietime','mtype','director','description','maincast','body','ytube','comments')

  