# ttranking/matches/tests.py

from django.test import TestCase
from players.models import Player
from .models import SinglesMatch, DoublesMatch, WINNING_POINTS, LOSING_POINTS


class MatchModelTestCase(TestCase):
    def setUp(self):
        # Create test players
        self.player1 = Player.objects.create(first_name="Player", last_name="One", ranking=0, matches_played=0)
        self.player2 = Player.objects.create(first_name="Player", last_name="Two", ranking=0, matches_played=0)
        self.player3 = Player.objects.create(first_name="Player", last_name="Three", ranking=0, matches_played=0)
        self.player4 = Player.objects.create(first_name="Player", last_name="Four", ranking=0, matches_played=0)

    def test_singles_match_creation_and_deletion(self):
        # Create a singles match
        match = SinglesMatch.objects.create(
            date="2024-08-20 10:00:00",
            player1=self.player1,
            player2=self.player2,
            player1_score=11,
            player2_score=9
        )

        # Verify points and match counts
        self.assertEqual(self.player1.ranking, 2)
        self.assertEqual(self.player2.ranking, 0)
        self.assertEqual(self.player1.matches_played, 1)
        self.assertEqual(self.player2.matches_played, 1)

        # Delete the match
        match.delete()

        # Verify points and match counts after deletion
        self.player1.refresh_from_db()
        self.player2.refresh_from_db()
        self.assertEqual(self.player1.ranking, 0)
        self.assertEqual(self.player2.ranking, 0)
        self.assertEqual(self.player1.matches_played, 0)
        self.assertEqual(self.player2.matches_played, 0)

    def test_doubles_match_creation_and_deletion(self):
        # Create a doubles match
        match = DoublesMatch.objects.create(
            date="2024-08-20 10:00:00",
            team1_player1=self.player1,
            team1_player2=self.player2,
            team2_player1=self.player3,
            team2_player2=self.player4,
            team1_score=11,
            team2_score=9
        )

        # Verify points and match counts
        self.assertEqual(self.player1.ranking, 2)
        self.assertEqual(self.player2.ranking, 2)
        self.assertEqual(self.player3.ranking, 0)
        self.assertEqual(self.player4.ranking, 0)
        self.assertEqual(self.player1.matches_played, 1)
        self.assertEqual(self.player2.matches_played, 1)
        self.assertEqual(self.player3.matches_played, 1)
        self.assertEqual(self.player4.matches_played, 1)

        # Delete the match
        match.delete()

        # Verify points and match counts after deletion
        self.player1.refresh_from_db()
        self.player2.refresh_from_db()
        self.player3.refresh_from_db()
        self.player4.refresh_from_db()
        self.assertEqual(self.player1.ranking, 0)
        self.assertEqual(self.player2.ranking, 0)
        self.assertEqual(self.player3.ranking, 0)
        self.assertEqual(self.player4.ranking, 0)
        self.assertEqual(self.player1.matches_played, 0)
        self.assertEqual(self.player2.matches_played, 0)
        self.assertEqual(self.player3.matches_played, 0)
        self.assertEqual(self.player4.matches_played, 0)

    def test_singles_match_update(self):
        # Create and update a singles match
        match = SinglesMatch.objects.create(
            date="2024-08-20 10:00:00",
            player1=self.player1,
            player2=self.player2,
            player1_score=11,
            player2_score=9
        )

        # Verify points and match counts after initial creation
        self.assertEqual(self.player1.ranking, 2)
        self.assertEqual(self.player2.ranking, 0)

        # Update the match score, making player 2 the winner
        match.player1_score = 9
        match.player2_score = 11
        print("Before saving match: ", match.player1.ranking, match.player2.ranking)
        match.save()
        print("After saving match: ", match.player1.ranking, match.player2.ranking)

        self.assertEqual(match.winner, self.player2)

        # Verify points after the update
        self.player1.refresh_from_db()
        self.player2.refresh_from_db()
        print(self.player1.ranking, self.player2.ranking)
        self.assertEqual(self.player1.ranking, 0)
        self.assertEqual(self.player2.ranking, 2)

    def test_doubles_match_update(self):
        # Create and update a doubles match
        match = DoublesMatch.objects.create(
            date="2024-08-20 10:00:00",
            team1_player1=self.player1,
            team1_player2=self.player2,
            team2_player1=self.player3,
            team2_player2=self.player4,
            team1_score=11,
            team2_score=9
        )

        # Verify points and match counts after initial creation
        self.assertEqual(self.player1.ranking, 2)
        self.assertEqual(self.player2.ranking, 2)
        self.assertEqual(self.player3.ranking, 0)
        self.assertEqual(self.player4.ranking, 0)

        # Update the match score, making Team 2 the winner
        match.team1_score = 9
        match.team2_score = 11
        match.save()

        # Verify points after the update
        self.player1.refresh_from_db()
        self.player2.refresh_from_db()
        self.player3.refresh_from_db()
        self.player4.refresh_from_db()
        self.assertEqual(self.player1.ranking, 0)
        self.assertEqual(self.player2.ranking, 0)
        self.assertEqual(self.player3.ranking, 2)
        self.assertEqual(self.player4.ranking, 2)
