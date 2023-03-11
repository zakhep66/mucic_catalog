# from django.contrib.auth.models import User
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase, APIClient
#
# from app.models import Category, Composition, Group, Artist, Role
#
#
# class CategoryTests(APITestCase):
# 	def setUp(self):
# 		self.user = User.objects.create_user(username='test_user', password='test_password')
# 		self.client = APIClient()
# 		self.client.force_authenticate(user=self.user)
#
# 		self.category = Category.objects.create(name='test_category')
# 		self.composition = Composition.objects.create(
# 			title='test_composition',
# 			description="test_description",
# 			category=self.category
# 		)
# 		self.group = Group.objects.create(
# 			name='test_group',
# 			description='test_description'
# 		)
# 		self.group.compositions.add(self.composition)
#
# 		self.role = Role.objects.create(name='test_role')
#
# 		self.artist = Artist.objects.create(
# 			name='test_artist',
# 			description='test_description',
# 			role=self.role
# 		)
# 		self.artist.groups.add(self.group)
#
# 	def test_get_categories(self):
# 		response = self.client.get(reverse('get_categories', kwargs={'pk': self.composition.pk}))
#
# 		self.assertEqual(response.status_code, status.HTTP_200_OK)
# 		self.assertEqual(response.data['name'], 'test_category')
#
# 	def test_get_role(self):
# 		response = self.client.get(reverse('get_role', kwargs={'pk': self.artist.pk}))
#
# 		self.assertEqual(response.status_code, status.HTTP_200_OK)
# 		self.assertEqual(response.data['name'], 'test_role')
#
# 	def test_add_composition(self):
# 		data = {'composition': self.composition.pk}
# 		response = self.client.post(reverse('add_composition', kwargs={'pk': self.composition.pk}), data)
#
# 		self.assertEqual(response.status_code, status.HTTP_200_OK)
# 		self.assertEqual(response.data, 'Composition added')
# 		self.assertEqual(self.group.compositions.count(), 1)
# 		self.assertEqual(self.group.compositions.get().title, 'test_composition')


########################################
########################################
########################################


from django.test import TestCase
from .models import Composition, Category, Group, Artist, Role


class CompositionModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(name='Rock')
        Composition.objects.create(title='Bohemian Rhapsody', description='One of the greatest songs ever made',
                                   category=category)

    def test_title_max_length(self):
        composition = Composition.objects.get(id=1)
        max_length = composition._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_title(self):
        composition = Composition.objects.get(id=1)
        expected_object_name = composition.title
        self.assertEquals(expected_object_name, str(composition))


class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='Pop')

    def test_name_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_name(self):
        category = Category.objects.get(id=1)
        expected_object_name = category.name
        self.assertEquals(expected_object_name, str(category))


class GroupModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(name='Rock')
        composition = Composition.objects.create(title='Stairway to Heaven',
                                                 description='One of the greatest rock songs ever made',
                                                 category=category)
        group = Group.objects.create(name='Led Zeppelin', description='One of the greatest rock bands ever made')
        group.compositions.add(composition)

    def test_name_max_length(self):
        group = Group.objects.get(id=1)
        max_length = group._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_name(self):
        group = Group.objects.get(id=1)
        expected_object_name = group.name
        self.assertEquals(expected_object_name, str(group))


class RoleModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Role.objects.create(name='Singer')

    def test_name_max_length(self):
        role = Role.objects.get(id=1)
        max_length = role._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_name(self):
        role = Role.objects.get(id=1)
        expected_object_name = role.name
        self.assertEquals(expected_object_name, str(role))


class ArtistModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        role = Role.objects.create(name='Guitarist')
        category = Category.objects.create(name='Rock')
        composition = Composition.objects.create(title='November Rain',
                                                 description='One of the greatest rock ballads ever made',
                                                 category=category)
        group = Group.objects.create(name='Guns N Roses', description='One of the greatest rock bands ever made')
        group.compositions.add(composition)
        artist = Artist.objects.create(name='Slash', description='One of the greatest guitarists ever', role=role)
        artist.groups.add(group)

    def test_name_max_length(self):
        artist = Artist.objects.get(id=1)
        max_length = artist._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_name(self):
        artist = Artist.objects.get(id=1)
        expected_object_name = artist.name
        self.assertEquals(expected_object_name, str(artist))
