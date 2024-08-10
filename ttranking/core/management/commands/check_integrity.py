from django.core.management import BaseCommand
from players.models import Player
from matches.models import SinglesMatch, DoublesMatch, WINNING_POINTS, LOSING_POINTS


class Command(BaseCommand):
    help = 'Check integrity of players\' data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--ranking',
            action='store_true',
            help='Check and update player rankings'
        )
        parser.add_argument(
            '--matchcount',
            action='store_true',
            help='Update match counts for each player'
        )
        # Add more arguments here as needed

    def handle(self, *args, **options):
        if options['ranking'] or options['matchcount']:
            self.stdout.write('You are about to make changes to the database.')
            self.stdout.write('Type Y to proceed, or any other key to cancel:')
            confirm = input().strip().upper()
            if confirm != 'Y':
                self.stdout.write('Operation canceled.')
                return

        if options['ranking']:
            self.check_ranking()
        if options['matchcount']:
            self.update_match_counts()
        # Add more options handling as needed

    def check_ranking(self):
        self.stdout.write('Checking player rankings...')
        for player in Player.objects.all():
            calculated_ranking = 0
            singles_matches = SinglesMatch.objects.all()
            for match in singles_matches:
                if player not in match.players:
                    continue
                if player != match.winner:
                    calculated_ranking -= LOSING_POINTS
                calculated_ranking += WINNING_POINTS

            doubles_matches = DoublesMatch.objects.all()
            for match in doubles_matches:
                if player not in match.players:
                    continue
                if player not in match.list_winners:
                    calculated_ranking -= LOSING_POINTS
                calculated_ranking += WINNING_POINTS

            if calculated_ranking != player.ranking:
                self.stdout.write(
                    f"Discrepancy found for {player}: expected {calculated_ranking}, found {player.ranking}")
                player.ranking = calculated_ranking
                player.save()

    def update_match_counts(self):
        self.stdout.write('Updating match counts for players...')
        for player in Player.objects.all():
            singles_match_count = SinglesMatch.objects.filter(
                player1=player
            ).count() + SinglesMatch.objects.filter(
                player2=player
            ).count()

            doubles_match_count = DoublesMatch.objects.filter(
                team1_player1=player
            ).count() + DoublesMatch.objects.filter(
                team1_player2=player
            ).count() + DoublesMatch.objects.filter(
                team2_player1=player
            ).count() + DoublesMatch.objects.filter(
                team2_player2=player
            ).count()

            total_match_count = singles_match_count + doubles_match_count

            player.matches_played = total_match_count
            player.save()
            self.stdout.write(f"Updated match count for {player}: {total_match_count}")
