from rest_framework import viewsets as v
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from app.models import Composition, Group, Artist
from app.serializers import CompositionSerializer, GroupSerializer, ArtistSerializer, CategorySerializer, RoleSerializer


class LimitOffsetPagination(PageNumberPagination):
	page_size_query_param = 'page_size'
	default_limit = 10


class CompositionViewSet(v.ModelViewSet):
	queryset = Composition.objects.all()
	serializer_class = CompositionSerializer
	pagination_class = LimitOffsetPagination

	@action(detail=False, methods=['get'])
	def get_categories(self, request, pk=None):
		composition = self.get_object()
		category = CategorySerializer(composition.category)
		return Response(category.data)


class GroupViewSet(v.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer
	pagination_class = LimitOffsetPagination

	@action(detail=False, methods=['post'])
	def add_composition(self, request, pk=None):
		groups = self.get_object()
		composition = Composition.objects.get(pk=request.data['composition'])
		groups.compositions.add(composition)
		return Response('Composition added')


class ArtistViewSet(v.ModelViewSet):
	queryset = Artist.objects.all()
	serializer_class = ArtistSerializer
	pagination_class = LimitOffsetPagination

	@action(detail=False, methods=['get'])
	def get_role(self, request, pk=None):
		artist = self.get_object()
		role = RoleSerializer(artist.role)
		return Response(role.data)
