from datetime import datetime
from django.db import models


class Season(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    @staticmethod
    def get_season_for_datetime(dt: datetime) -> 'Season':
        """
        Returns the season for the given date. If the date is not within any season, returns None.
        :param date: The date (with or without time) to find the season for.
        :return: The season for the given date, or None if no season matches.
        """
        date_only = dt.date()
        return Season.objects.filter(start_date__lte=date_only, end_date__gte=date_only).first()

    def __str__(self):
        return self.name
