# ttranking/matches/tests.py

from django.test import TestCase
from players.models import Player
from .models import SinglesMatch, DoublesMatch


class PlayerModelTests(TestCase):
    def setUp(self):
        # Create players for testing
        self.player1 = Player.objects.create(first_name="Player 1")
        self.player2 = Player.objects.create(first_name="Player 2")
        self.player3 = Player.objects.create(first_name="Player 3")
        self.player4 = Player.objects.create(first_name="Player 4")


class SinglesMatchModelTests(PlayerModelTests):
    def test_create_singles_match(self):
        match = SinglesMatch.objects.create(
            date="2024-08-03T12:00:00Z",
            player1=self.player1,
            player2=self.player2,
            player1_score=11,
            player2_score=2
        )
        self.assertEqual(match.player1_score, 11)
        self.assertEqual(match.player2_score, 2)
        self.assertEqual(match.winner, self.player1)
        self.assertEqual(self.player1.ranking, 1)
        self.assertEqual(self.player2.ranking, 0)

    def test_update_singles_match(self):
        match = SinglesMatch.objects.create(
            date="2024-08-03T12:00:00Z",
            player1=self.player1,
            player2=self.player2,
            player1_score=11,
            player2_score=10
        )
        self.assertEqual(match.winner, None)

        # now enter a correct score
        match.player1_score = 12
        match.save()

        self.assertEqual(match.player1_score, 12)
        self.assertEqual(match.winner, self.player1)
        self.assertEqual(self.player1.ranking, 1)  # Points should be deducted
        self.assertEqual(self.player2.ranking, 0)

    def test_determine_winner(self):
        match = SinglesMatch.objects.create(
            date="2024-08-03T12:00:00Z",
            player1=self.player1,
            player2=self.player2,
            player1_score=11,
            player2_score=2
        )
        self.assertEqual(match.winner, self.player1)

class DoublesMatchModelTests(PlayerModelTests):
    def test_create_doubles_match(self):
        match = DoublesMatch.objects.create(
            date="2024-08-03T12:00:00Z",
            team1_player1=self.player1,
            team1_player2=self.player2,
            team2_player1=self.player3,
            team2_player2=self.player4,
            team1_score=11,
            team2_score=2
        )
        self.assertEqual(match.team1_score, 11)
        self.assertEqual(match.team2_score, 2)
        self.assertEqual(match.winner_team, "Team 1")
        self.assertEqual(self.player1.ranking, 1)
        self.assertEqual(self.player2.ranking, 1)
        self.assertEqual(self.player3.ranking, 0)
        self.assertEqual(self.player4.ranking, 0)

    def test_update_doubles_match(self):
        match = DoublesMatch.objects.create(
            date="2024-08-03T12:00:00Z",
            team1_player1=self.player1,
            team1_player2=self.player2,
            team2_player1=self.player3,
            team2_player2=self.player4,
            team1_score=11,
            team2_score=2
        )
        self.assertEqual(match.winner_team, "Team 1")
        self.assertEqual(self.player1.ranking, 1)  # Points should be deducted
        self.assertEqual(self.player2.ranking, 1)
        self.assertEqual(self.player3.ranking, 0)
        self.assertEqual(self.player4.ranking, 0)

    def test_determine_winner_team(self):
        match = DoublesMatch(
            date="2024-08-03T12:00:00Z",
            team1_player1=self.player1,
            team1_player2=self.player2,
            team2_player1=self.player3,
            team2_player2=self.player4,
            team1_score=3,
            team2_score=2
        )
        self.assertEqual(match.winner_team, None)
