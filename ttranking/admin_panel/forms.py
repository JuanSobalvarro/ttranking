# ttranking/players/forms.py
from django import forms
from django.core.exceptions import ValidationError
import imghdr

from players.models import Player, COUNTRY_CHOICES
from matches.models import SinglesMatch, DoublesMatch

import datetime
