from datetime import date
from django.db import models


class Season(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    @staticmethod
    def get_season_for_date(date: date):
        """
        Returns the season for the given date. if the date is not within any season, returns None.
        :param date:
        :return:
        """
        return Season.objects.filter(start_date__lte=date, end_date__gte=date).first()

    def __str__(self):
        return self.name
