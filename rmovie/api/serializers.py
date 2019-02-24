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
  # comm = MovieSerializer(required=True)
  class Meta(object):
    model = Detai
    fields = ('pk','name','Status','Language','Budget','Revenue','Production_Companies','Production_Country','adult')

  # def create(self, validated_data):
  #     """
  #     Overriding the default create method of the Model serializer.
  #     :param validated_data: data containing all the details of student
  #     :return: returns a successfully created student record
  #     """
  #     user_data = validated_data.pop('comm')
  #     user = MovieSerializer.create(MovieSerializer(), validated_data=user_data)
  #     student, created = Detai.objects.update_or_create(user=user,
  #                         subject_major=validated_data.pop('subject_major'))
  #     return student


class MovieDetailsSerializer(serializers.ModelSerializer):
  comments = CastSerializer(many=True)
  # details = DetailSerializer(many=True)
  class Meta(object):
    model = Moviee
    fields = ('name','mdate','rating','murl','movietime','mtype','director','description','maincast','body','ytube','comments')


class MovieDetailsSerializer1(serializers.ModelSerializer):

  class Meta(object):
    model = Moviee
    fields = ('name','mdate','rating','murl','movietime','mtype','director','description','maincast','body','ytube')

  