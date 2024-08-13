# ttranking/api/tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from players.models import Player
from matches.models import SinglesMatch, DoublesMatch


class PlayerAPITests(APITestCase):

    def setUp(self):
        # Create a user and authenticate
        self.user = User.objects.create_user(username='testuser', password='testpass', is_staff=True)
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')

        # Create some players for testing
        self.player_1 = Player.objects.create(first_name="John", last_name="Doe")
        self.player_2 = Player.objects.create(first_name="Jane", last_name="Smith")

    def test_list_players(self):
        url = reverse('api:player_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_player(self):
        url = reverse('api:player_detail', kwargs={'pk': self.player_1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], self.player_1.first_name)

    def test_create_player(self):
        url = reverse('api:player_list')
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "alias": "Ali",
            "gender": "M",
            "date_of_birth": "01/01/1999",
            "nationality": "US",
            "ranking": 1000,
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Player.objects.count(), 3)
        self.assertEqual(Player.objects.last().first_name, "John")

    def test_update_player(self):
        url = reverse('api:player_detail', kwargs={'pk': self.player_1.pk})
        data = {'first_name': 'John', 'last_name': 'Updated'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.player_1.refresh_from_db()
        self.assertEqual(self.player_1.last_name, 'Updated')

    def test_delete_player(self):
        url = reverse('api:player_detail', kwargs={'pk': self.player_1.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Player.objects.count(), 1)

    def test_not_allowed_methods(self):
        url = reverse('api:player_list')
        response = self.client.put(url)  # PUT on a list endpoint should not be allowed
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class SinglesMatchAPITests(APITestCase):
    pass


class DoublesMatchAPITests(APITestCase):
    pass

