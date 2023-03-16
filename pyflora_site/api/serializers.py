from statistics import mode
from rest_framework import serializers

from pyflora_app.models import Plant, Stats, Pot

class PlantSerializer(serializers.ModelSerializer):
    plant_photo = serializers.ImageField(required=False, max_length=None, 
                                     allow_empty_file=True, use_url=True)

    class Meta:
        model = Plant
        fields = ('plant_name','plant_photo','plant_care_humidity', 'plant_care_light', 'plant_care_minerals','plant_care_ph')

class StatusSerializer(serializers.ModelSerializer):
    plant_humidity = serializers.IntegerField(source='plant_id.plant_care_humidity')
    plant_lux = serializers.IntegerField(source='plant_id.plant_care_light')
    plant_ph = serializers.IntegerField(source='plant_id.plant_care_ph')
    plant_minerals = serializers.FloatField(source='plant_id.plant_care_minerals')

    class Meta:
        model = Stats
        fields = '__all__'

class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stats
        fields = '__all__'

class PotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pot
        fields = ('id', 'plants_pot')

class PlantStatsSerialize(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ('pk','plant_care_humidity', 'plant_care_light', 'plant_care_minerals', 'plant_care_ph')