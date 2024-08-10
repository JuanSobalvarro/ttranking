# api/tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from players.models import Player
from matches.models import SinglesMatch, DoublesMatch


class PlayerAPITests(APITestCase):

    def setUp(self):
        # Create a user and authenticate
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')

        # Create some players for testing
        self.player_1 = Player.objects.create(first_name="John", last_name="Doe")
        self.player_2 = Player.objects.create(first_name="Jane", last_name="Smith")

    def test_list_players(self):
        url = rever
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



# class SinglesMatchAPITests(APITestCase):
#
#     def setUp(self):
#         # Create a user and authenticate
#         self.user = User.objects.create_user(username='testuser', password='testpass')
#         self.client = APIClient()
#         self.client.login(username='testuser', password='testpass')
#
#         # Create some players and a singles match
#         self.player_1 = Player.objects.create(first_name="John", last_name="Doe")
#         self.player_2 = Player.objects.create(first_name="Jane", last_name="Smith")
#         self.singles_match = SinglesMatch.objects.create(player_1=self.player_1, player_2=self.player_2, score="11-9")
#
#     def test_list_singles_matches(self):
#         url = reverse('api:api_singles_matches-list')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_retrieve_singles_match(self):
#         url = reverse('api:api_singles_matches-detail', args=[self.singles_match.id])
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['score'], self.singles_match.score)
#
#     def test_create_singles_match(self):
#         url = reverse('api:api_singles_matches-list')
#         data = {
#             'player_1': self.player_1.id,
#             'player_2': self.player_2.id,
#             'score': '11-7'
#         }
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(SinglesMatch.objects.count(), 2)
#
#     def test_update_singles_match(self):
#         url = reverse('api:api_singles_matches-detail', args=[self.singles_match.id])
#         data = {
#             'player_1': self.player_1.id,
#             'player_2': self.player_2.id,
#             'score': '11-5'
#         }
#         response = self.client.put(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.singles_match.refresh_from_db()
#         self.assertEqual(self.singles_match.score, '11-5')
#
#     def test_delete_singles_match(self):
#         url = reverse('api:api_singles_matches-detail', args=[self.singles_match.id])
#         response = self.client.delete(url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(SinglesMatch.objects.count(), 0)
#
#
# class DoublesMatchAPITests(APITestCase):
#
#     def setUp(self):
#         # Create a user and authenticate
#         self.user = User.objects.create_user(username='testuser', password='testpass')
#         self.client = APIClient()
#         self.client.login(username='testuser', password='testpass')
#
#         # Create some players and a doubles match
#         self.player_1 = Player.objects.create(first_name="John", last_name="Doe")
#         self.player_2 = Player.objects.create(first_name="Jane", last_name="Smith")
#         self.player_3 = Player.objects.create(first_name="Alice", last_name="Johnson")
#         self.player_4 = Player.objects.create(first_name="Bob", last_name="Brown")
#         self.doubles_match = DoublesMatch.objects.create(player_1=self.player_1, player_2=self.player_2,
#                                                          player_3=self.player_3, player_4=self.player_4, score="11-8")
#
#     def test_list_doubles_matches(self):
#         url = reverse('api:api_doubles_matches-list')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_retrieve_doubles_match(self):
#         url = reverse('api:api_doubles_matches-detail', args=[self.doubles_match.id])
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['score'], self.doubles_match.score)
#
#     def test_create_doubles_match(self):
#         url = reverse('api:api_doubles_matches-list')
#         data = {
#             'player_1': self.player_1.id,
#             'player_2': self.player_2.id,
#             'player_3': self.player_3.id,
#             'player_4': self.player_4.id,
#             'score': '11-9'
#         }
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(DoublesMatch.objects.count(), 2)
#
#     def test_update_doubles_match(self):
#         url = reverse('api:api_doubles_matches-detail', args=[self.doubles_match.id])
#         data = {
#             'player_1': self.player_1.id,
#             'player_2': self.player_2.id,
#             'player_3': self.player_3.id,
#             'player_4': self.player_4.id,
#             'score': '11-6'
#         }
#         response = self.client.put(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.doubles_match.refresh_from_db()
#         self.assertEqual(self.doubles_match.score, '11-6')
#
#     def test_delete_doubles_match(self):
#         url = reverse('api:api_doubles_matches-detail', args=[self.doubles_match.id])
#         response = self.client.delete(url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(DoublesMatch.objects.count(), 0)
