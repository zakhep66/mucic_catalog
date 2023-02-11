from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from app.models import Category, Composition, Group, Artist, Role


class CategoryTests(APITestCase):
	def setUp(self):
		self.user = User.objects.create_user(username='test_user', password='test_password')
		self.client = APIClient()
		self.client.force_authenticate(user=self.user)

		self.category = Category.objects.create(name='test_category')
		self.composition = Composition.objects.create(
			title='test_composition',
			description="test_description",
			category=self.category
		)
		self.group = Group.objects.create(
			name='test_group',
			description='test_description'
		)
		self.group.compositions.add(self.composition)

		self.role = Role.objects.create(name='test_role')

		self.artist = Artist.objects.create(
			name='test_artist',
			description='test_description',
			role=self.role
		)
		self.artist.groups.add(self.group)

	def test_get_categories(self):
		response = self.client.get(reverse('get_categories', kwargs={'pk': self.composition.pk}))

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['name'], 'test_category')

	def test_get_role(self):
		response = self.client.get(reverse('get_role', kwargs={'pk': self.artist.pk}))

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['name'], 'test_role')

	def test_add_composition(self):
		data = {'composition': self.composition.pk}
		response = self.client.post(reverse('add_composition', kwargs={'pk': self.composition.pk}), data)

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data, 'Composition added')
		self.assertEqual(self.group.compositions.count(), 1)
		self.assertEqual(self.group.compositions.get().title, 'test_composition')
