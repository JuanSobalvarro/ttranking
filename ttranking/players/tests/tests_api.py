from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from players.models import Player


class PlayerAPITestCase(APITestCase):
    def setUp(self):
        # Create a few Player instances to test
        self.player1 = Player.objects.create(first_name='Player One', ranking=100)
        self.player2 = Player.objects.create(first_name='Player Two', ranking=110)
        self.player_list_url = reverse('players_api:player_list')
        self.player_detail_url = lambda pk: reverse('players_api:player_detail', kwargs={'pk': pk})

    def test_get_player_list(self):
        response = self.client.get(self.player_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_player_detail(self):
        response = self.client.get(self.player_detail_url(self.player1.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], self.player1.first_name)

    def test_post_not_allowed(self):
        data = {
            'first_name': 'Player Three',
            'ranking': 120
        }
        response = self.client.post(self.player_list_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_not_allowed(self):
        data = {
            'first_name': 'Updated Name',
            'ranking': 120
        }
        response = self.client.put(self.player_detail_url(self.player1.pk), data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_not_allowed(self):
        response = self.client.delete(self.player_detail_url(self.player1.pk))
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)