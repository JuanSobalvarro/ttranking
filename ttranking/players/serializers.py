from rest_framework import serializers
from .models import Player
import math


class PlayerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    winrate = serializers.SerializerMethodField()
    victories = serializers.SerializerMethodField()

    class Meta:
        model = Player
        fields = '__all__'  # or specify fields explicitly like ['id', 'name', 'age', 'team']

    def get_winrate(self, obj):
        if obj.matches_played == 0:
            return 0
        return obj.winrate

    def get_victories(self, obj):
        return obj.victories