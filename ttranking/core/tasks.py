# core/tasks.py
import time
from celery import shared_task
import matches
import players


@shared_task
def check_integrity():
    for player in players.Player.objects.all():
        calculated_ranking = 0
        singlesMatches = matches.SinglesMatch.objects.filter(player=player)
        for match in singlesMatches:
            if player not in match.players:
                continue
            if player != match.winner:
                calculated_ranking -= matches.LOSING_POINTS

            calculated_ranking += matches.WINNING_POINTS

        doublesMatches = matches.DoublesMatch.objects.filter(player=player)
        for match in doublesMatches:
            if player not in match.players:
                continue
            if player not in match.list_winners:
                calculated_ranking -= matches.LOSING_POINTS

            calculated_ranking += matches.WINNING_POINTS

        if calculated_ranking != player.ranking:
            print(f"Discrepancy found for {player}: expected {calculated_ranking}, found {player.ranking}")
            # Handle the discrepancy (e.g., send an alert, auto-correct, etc.)

@shared_task
def test_task():
    time.sleep(10)  # Simulate a long-running task
    return "Task completed"