# ttranking/matches/tests.py
from datetime import datetime
from django.utils import timezone

from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from matches.models import SinglesMatch, DoublesMatch, WINNING_POINTS, LOSING_POINTS
from players.models import Player
from seasons.models import Season


# class MatchModelTestCase(TestCase):
#     def setUp(self):
#         # Create test players
#         self.player1 = Player.objects.create(first_name="Player", last_name="One", ranking=0, matches_played=0)
#         self.player2 = Player.objects.create(first_name="Player", last_name="Two", ranking=0, matches_played=0)
#         self.player3 = Player.objects.create(first_name="Player", last_name="Three", ranking=0, matches_played=0)
#         self.player4 = Player.objects.create(first_name="Player", last_name="Four", ranking=0, matches_played=0)
#
#         # Create a season for the matches
#         self.season = Season.objects.create(name="2024 Season", start_date="2024-01-01", end_date="2024-12-31")
#
#     def test_singles_match_creation_and_deletion(self):
#         # Create a singles match with a season
#         match = SinglesMatch.objects.create(
#             date="2024-08-20 10:00:00",
#             season=self.season,  # include the season
#             player1=self.player1,
#             player2=self.player2,
#             player1_score=11,
#             player2_score=9
#         )
#
#         # Verify points and match counts
#         self.assertEqual(self.player1.ranking, 2)
#         self.assertEqual(self.player2.ranking, 0)
#         self.assertEqual(self.player1.matches_played, 1)
#         self.assertEqual(self.player2.matches_played, 1)
#
#         # Delete the match
#         match.delete()
#
#         # Verify points and match counts after deletion
#         self.player1.refresh_from_db()
#         self.player2.refresh_from_db()
#         self.assertEqual(self.player1.ranking, 0)
#         self.assertEqual(self.player2.ranking, 0)
#         self.assertEqual(self.player1.matches_played, 0)
#         self.assertEqual(self.player2.matches_played, 0)
#
#     def test_doubles_match_creation_and_deletion(self):
#         # Create a doubles match with a season
#         match = DoublesMatch.objects.create(
#             date="2024-08-20 10:00:00",
#             season=self.season,  # include the season
#             team1_player1=self.player1,
#             team1_player2=self.player2,
#             team2_player1=self.player3,
#             team2_player2=self.player4,
#             team1_score=11,
#             team2_score=9
#         )
#
#         # Verify points and match counts
#         self.assertEqual(self.player1.ranking, 2)
#         self.assertEqual(self.player2.ranking, 2)
#         self.assertEqual(self.player3.ranking, 0)
#         self.assertEqual(self.player4.ranking, 0)
#         self.assertEqual(self.player1.matches_played, 1)
#         self.assertEqual(self.player2.matches_played, 1)
#         self.assertEqual(self.player3.matches_played, 1)
#         self.assertEqual(self.player4.matches_played, 1)
#
#         # Delete the match
#         match.delete()
#
#         # Verify points and match counts after deletion
#         self.player1.refresh_from_db()
#         self.player2.refresh_from_db()
#         self.player3.refresh_from_db()
#         self.player4.refresh_from_db()
#         self.assertEqual(self.player1.ranking, 0)
#         self.assertEqual(self.player2.ranking, 0)
#         self.assertEqual(self.player3.ranking, 0)
#         self.assertEqual(self.player4.ranking, 0)
#         self.assertEqual(self.player1.matches_played, 0)
#         self.assertEqual(self.player2.matches_played, 0)
#         self.assertEqual(self.player3.matches_played, 0)
#         self.assertEqual(self.player4.matches_played, 0)
#
#     def test_singles_match_update(self):
#         # Create and update a singles match with a season
#         match = SinglesMatch.objects.create(
#             date="2024-08-20 10:00:00",
#             season=self.season,  # include the season
#             player1=self.player1,
#             player2=self.player2,
#             player1_score=11,
#             player2_score=9
#         )
#
#         # Verify points and match counts after initial creation
#         self.assertEqual(self.player1.ranking, 2)
#         self.assertEqual(self.player2.ranking, 0)
#
#         # Update the match score, making player 2 the winner
#         match.player1_score = 9
#         match.player2_score = 11
#         match.save()
#
#         self.assertEqual(match.winner, self.player2)
#
#         # Verify points after the update
#         self.player1.refresh_from_db()
#         self.player2.refresh_from_db()
#         self.assertEqual(self.player1.ranking, 0)
#         self.assertEqual(self.player2.ranking, 2)
#
#     def test_doubles_match_update(self):
#         # Create and update a doubles match with a season
#         match = DoublesMatch.objects.create(
#             date="2024-08-20 10:00:00",
#             season=self.season,  # include the season
#             team1_player1=self.player1,
#             team1_player2=self.player2,
#             team2_player1=self.player3,
#             team2_player2=self.player4,
#             team1_score=11,
#             team2_score=9
#         )
#
#         # Verify points and match counts after initial creation
#         self.assertEqual(self.player1.ranking, 2)
#         self.assertEqual(self.player2.ranking, 2)
#         self.assertEqual(self.player3.ranking, 0)
#         self.assertEqual(self.player4.ranking, 0)
#
#         # Update the match score, making Team 2 the winner
#         match.team1_score = 9
#         match.team2_score = 11
#         match.save()
#
#         # Verify points after the update
#         self.player1.refresh_from_db()
#         self.player2.refresh_from_db()
#         self.player3.refresh_from_db()
#         self.player4.refresh_from_db()
#         self.assertEqual(self.player1.ranking, 0)
#         self.assertEqual(self.player2.ranking, 0)
#         self.assertEqual(self.player3.ranking, 2)
#         self.assertEqual(self.player4.ranking, 2)


class MatchAPITests(APITestCase):
    def setUp(self):
        # Create users and players
        self.admin_user = User.objects.create_superuser('admin', '', 'admin')
        self.user = User.objects.create_user('user', '', 'user')
        # Create players with the correct fields
        self.player1 = Player.objects.create(
            first_name="John",
            last_name="Doe",
            alias="JD",
            gender="M",
            date_of_birth="1990-01-01",
            nationality="US",
        )
        self.player2 = Player.objects.create(
            first_name="Jane",
            last_name="Smith",
            alias="JS",
            gender="F",
            date_of_birth="1992-02-02",
            nationality="GB",
        )
        self.player3 = Player.objects.create(
            first_name="Michael",
            last_name="Johnson",
            alias="MJ",
            gender="M",
            date_of_birth="1988-03-03",
            nationality="CA",
        )
        self.player4 = Player.objects.create(
            first_name="Emily",
            last_name="Davis",
            alias="ED",
            gender="F",
            date_of_birth="1995-04-04",
            nationality="AU",
        )

        # Get tokens for authentication
        self.token_admin = self.get_token('admin', 'admin')
        self.token_user = self.get_token('user', 'user')

    def get_token(self, username, password):
        url = reverse('core:api_token')
        data = {'username': username, 'password': password}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data['access']

    def test_create_singles_match_unauthenticated(self):
        url = reverse('matches:singlesmatch-list')
        data = {
            'date': timezone.make_aware(datetime.strptime('2024-08-20T10:00:00Z', '%Y-%m-%dT%H:%M:%SZ')),
            'player1': self.player1.id,
            'player2': self.player2.id,
            'player1_score': 11,
            'player2_score': 9
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_singles_match_authenticated(self):
        url = reverse('matches:singlesmatch-list')
        data = {
            'date': timezone.make_aware(datetime.strptime('2024-08-20T10:00:00Z', '%Y-%m-%dT%H:%M:%SZ')),
            'player1': self.player1.id,
            'player2': self.player2.id,
            'player1_score': 11,
            'player2_score': 9
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_singles_match_admin(self):
        url = reverse('matches:singlesmatch-list')
        data = {
            'date': timezone.make_aware(datetime.strptime('2024-08-20T10:00:00Z', '%Y-%m-%dT%H:%M:%SZ')),
            'player1': self.player1.id,
            'player2': self.player2.id,
            'player1_score': 11,
            'player2_score': 9
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_admin)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['player1'], self.player1.id)
        self.assertEqual(response.data['player2'], self.player2.id)

    def test_retrieve_singles_match(self):
        match = SinglesMatch.objects.create(
            date=timezone.make_aware(datetime.strptime("2024-08-20T10:00:00Z", '%Y-%m-%dT%H:%M:%SZ')),
            player1=self.player1,
            player2=self.player2,
            player1_score=11,
            player2_score=9
        )
        url = reverse('matches:singlesmatch-detail', args=[match.id])

        # Unauthenticated test
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Authenticated as user
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['player1'], self.player1.id)

        # Authenticated as admin
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_admin)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['player1'], self.player1.id)

    def test_update_singles_match(self):
        match = SinglesMatch.objects.create(
            date=timezone.make_aware(datetime.strptime("2024-08-20T10:00:00Z", '%Y-%m-%dT%H:%M:%SZ')),
            player1=self.player1,
            player2=self.player2,
            player1_score=11,
            player2_score=9
        )
        url = reverse('matches:singlesmatch-detail', args=[match.id])
        data = {'player1_score': 15}

        # Unauthenticated test
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Authenticated as user
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_user)
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Authenticated as admin
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_admin)
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['player1_score'], 15)

    def test_delete_singles_match(self):
        match = SinglesMatch.objects.create(
            date=timezone.make_aware(datetime.strptime("2024-08-20T10:00:00Z", '%Y-%m-%dT%H:%M:%SZ')),
            player1=self.player1,
            player2=self.player2,
            player1_score=11,
            player2_score=9
        )
        url = reverse('matches:singlesmatch-detail', args=[match.id])

        # Unauthenticated test
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Authenticated as user
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Authenticated as admin
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_admin)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
