from django.db import models
from django.urls import reverse
from django.utils import timezone

class Pot(models.Model):
    pot_name = models.CharField(max_length=32)
    #plant_planted = models.CharField(max_length=32)
    plants_pot = models.ForeignKey('Plant', on_delete=models.CASCADE, blank=True, null=True, related_name="plants", related_query_name="plant")
    
    def get_absolute_url(self):
        return reverse('pot-update',kwargs={'pk':self.pk})
    def __str__(self):
         return f'{self.pot_name}'

class Plant(models.Model):
    plant_name = models.CharField(max_length=32)
    plant_photo = models.ImageField(blank=True)
    plant_care_humidity = models.IntegerField(null=True, blank=True)
    plant_care_light = models.IntegerField(null=True, blank=True)
    plant_care_minerals = models.FloatField(null=True, blank=True)
    plant_care_ph = models.IntegerField(null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse('plant-detail', kwargs={'pk': self.pk})

    def __str__(self):
         return f'{self.plant_name}'

class Stats(models.Model):
    stats_time = models.DateTimeField(default=timezone.now)
    pot_senzors_id = models.ForeignKey('Pot', on_delete=models.CASCADE, blank=True, null=True, db_constraint=False, related_name='stats')
    plant_id = models.ForeignKey('Plant', on_delete=models.CASCADE, blank=True, null=True, db_constraint=False, related_name='plant_stats')
    humidity_status = models.IntegerField()
    lux_status = models.IntegerField()
    minerals = models.FloatField()
    ph = models.IntegerField(null=True)

    class Meta:
        ordering = ['-stats_time']
        get_latest_by = 'stats_time'

    def __str__(self):
         return f'{self.stats_time}'
