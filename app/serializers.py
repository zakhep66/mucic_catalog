from rest_framework import serializers as s

from app.models import Composition, Category, Group, Artist, Role


class CompositionSerializer(s.ModelSerializer):
	class Meta:
		model = Composition
		fields = '__all__'


class CategorySerializer(s.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'


class GroupSerializer(s.ModelSerializer):
	class Meta:
		model = Group
		fields = '__all__'


class ArtistSerializer(s.ModelSerializer):
	class Meta:
		model = Artist
		fields = '__all__'


class RoleSerializer(s.ModelSerializer):
	class Meta:
		model = Role
		fields = '__all__'
