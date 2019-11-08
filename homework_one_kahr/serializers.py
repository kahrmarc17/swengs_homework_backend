from rest_framework import serializers
from . import models


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Animal
        fields = ['id', 'name', 'family', 'category', 'origin_land', 'date_of_birth', 'age', 'food', 'zoo', 'zookeeper']


