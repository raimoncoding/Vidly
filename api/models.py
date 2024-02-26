from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie
from props.models import Prop


class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movies'


class PropResource(ModelResource):
    class Meta:
        queryset = Prop.objects.all()
        resource_name = 'props'
