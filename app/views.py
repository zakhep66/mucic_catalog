from rest_framework import viewsets as v
from rest_framework.decorators import action
from rest_framework.response import Response

from app.models import Composition, Group, Artist
from app.serializers import CompositionSerializer, GroupSerializer, ArtistSerializer


class CompositionViewSet(v.ModelViewSet):
	queryset = Composition.objects.all()
	serializer_class = CompositionSerializer


# todo: добавить action на get запрос, который будет возвращать список категорий, которые относятся к композиции
# todo: добавить action на post запрос, который будет добавлять категорию к композиции


class GroupViewSet(v.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer


class ArtistViewSet(v.ModelViewSet):
	queryset = Artist.objects.all()
	serializer_class = ArtistSerializer

# todo: добавить action на get запрос, который будет возвращать роль исполнителя
