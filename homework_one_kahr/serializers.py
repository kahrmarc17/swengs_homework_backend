from rest_framework import serializers
from . import models


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Animal
        fields = ['id', 'family', 'category', 'name', 'origin_land', 'date_of_birth', 'age', 'food', 'zoo', 'zookeeper']


class ZooSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Zoo
        fields = ['id', 'name', 'address', 'postal_code', 'town', 'land', 'telephone_number', 'mail']


class ZookeeperSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Zookeeper
        fields = ['id', 'first_name', 'last_name', 'date_of_birth', 'adjusted_since', 'salary', 'telephone_number']

